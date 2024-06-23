from IPython.core.magic import register_cell_magic
import paramiko
from scp import SCPClient
import os
import sys
import functools
import dill
import IPython

import json
def load_json(file_path):
    """
    加载JSON文件
    file_path：JSON文件的路径
    返回：JSON文件中的内容，以字典形式返回
    """
    with open(file_path, 'r') as f:
        v = json.load(f)
    return v
__registerd_nodes = load_json('/packages/registerd.json') #8840




__cells_temprate = """
import dill
with open('{}', 'rb') as f:
    dicts = dill.load(f)
    locals().update(dicts)
    del f
#print(dicts)
{}
params_dict = dict(locals())
params_dict.pop('dicts')

#返回变量
with open('{}', 'wb') as f:
    dill.dump(params_dict,f)
        """

def __check_line(line):
    if __registerd_nodes.get(line,None):
        return __registerd_nodes[line]
    else:
        raise Exception(f'已注册的有&& {list(__registerd_nodes.keys())} &&')
            
def __build(host):
    # 创建SSH客户端并连接到服务器
    #host = os.environ.get('computer_host','192.168.8.125_126')
    username = os.environ.get('computer_username','qe')
    password = os.environ.get('computer_password','qe1234')
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(host, username=username, password=password)
    return ssh_client


def __runs(ssh_client,command):
    # 通过SSH连接发送命令
    stdin, stdout, stderr = ssh_client.exec_command(command)
    # 获取命令执行的输出和错误
    output = stdout.read().decode()
    errors = stderr.read().decode()
    return output,errors


def __save_params(temp_params_path):
    # 假设您有一个名为fib(n)的函数，用于计算斐波那契数列的第n项
    ip = IPython.get_ipython()
    params = {k: v for k, v in ip.user_ns.items() if
              (not k.startswith('_') and k not in ['In', 'Out', 'exit', 'quit', 'open', 'get_ipython',
                                                  'register_cell_magic','paramiko','SCPClient','sys',
                                                  'dill','IPython','__build','__runs','ssh_computer',
                                                   '__check_line','qenode','qenodeplus','get_params','tknode',
                                                   'load_ipython_extension','os','functools'
                                                  ])}
    with open(temp_params_path, 'wb') as f:
        dill.dump(params, f)
def __load_params(local_params):
    with open(local_params, 'rb') as f:
        dicts = dill.load(f)
        ip = IPython.get_ipython()
        ip.user_ns.update(dicts)
@register_cell_magic
def node(line,cell):
    """
    node_local_file : 环境变量 指定主机的缓存文件位置 
    slave_file : 环境变量 指定从机的缓存文件位置 
    slave_docker_file:
    """    
    local_file = os.environ.get('node_local_file',os.path.join(os.getcwd(),'.computer_temp.py'))
    slave_file = os.environ.get('slave_file',os.path.join(os.getcwd(),'/qe/data/data/.temp.py'))
    slave_docker_file = '/root/temp.py' #从机docker文件
    local_params = os.path.join(local_file.rsplit('/',1)[0],'.params_path') #主机变量位置
    slave_params = os.path.join(slave_file.rsplit('/',1)[0],'.params_path') #从机变量位置
    slave_docker_params = '/root/temp.params_path' #从机docker变量
    # 检查参数
    infos = __check_line(line)

    #保存参数
    __save_params(local_params)
    
    slave_docker_params_ = slave_docker_params+'_'
    slave_params_ = slave_params+'_'
    local_params_ = local_params+'_'
    #保存代码
    cells = __cells_temprate.format(slave_docker_params,cell,slave_docker_params_)
    with open(local_file, 'w') as f:
        f.write(cells)
    
    #传输
    ssh_client = __build(infos['host'])
    with SCPClient(ssh_client.get_transport()) as scp:
        scp.put(local_file, slave_file)
        scp.put(local_params,slave_params)
            
    
    __runs(ssh_client,f'docker cp {slave_file} {infos["container"]}:{slave_docker_file}')
    __runs(ssh_client,f'docker cp {slave_params} {infos["container"]}:{slave_docker_params}')
    
    kernel_name = os.path.basename(sys.executable.replace("/bin/python",""))
    if kernel_name == 'py310':
        output,errors = __runs(ssh_client,f'docker exec {infos["container"]} /bin/bash -c "/opt/conda/envs/py310/bin/python /root/temp.py"')
    elif kernel_name == 'conda':
        output,errors = __runs(ssh_client,f'docker exec {infos["container"]} /bin/bash -c "/opt/conda/bin/python /root/temp.py"')
    #拉取docker 文件 dockerfiles cp mycontainer:/opt/test.txt /home/user
    
    __runs(ssh_client,f'docker cp {infos["container"]}:{slave_docker_params_} {slave_params_}')
    
    with SCPClient(ssh_client.get_transport()) as scp:
        scp.get(slave_params_, local_params_)
        
    __load_params(local_params_)
    # 关闭SSH连接
    ssh_client.close()

    if errors:
        raise Exception(errors)
    else:
        print(output)



@register_cell_magic
def nodeold(line,cell):
    """
    node_local_file : 环境变量 指定主机的缓存文件位置 
    slave_file : 环境变量 指定从机的缓存文件位置 
    slave_docker_file:
    """    
    local_file = os.environ.get('node_local_file',os.path.join(os.getcwd(),'.computer_temp.py'))
    slave_file = os.environ.get('slave_file',os.path.join(os.getcwd(),'/qe/data/data/.temp.py'))
    slave_docker_file = '/root/temp.py' #从机docker文件
    infos = __check_line(line)
    
    with open(local_file,'w') as f:
        f.write(cell)
        
    ssh_client = __build(infos['host'])
    with SCPClient(ssh_client.get_transport()) as scp:
        scp.put(local_file, slave_file)

    __runs(ssh_client,f'docker cp {slave_file} {infos["container"]}:{slave_docker_file}')
    kernel_name = os.path.basename(sys.executable.replace("/bin/python",""))
    if kernel_name == 'py310':
        output,errors = __runs(ssh_client,f'docker exec {infos["container"]} /bin/bash -c "/opt/conda/envs/py310/bin/python /root/temp.py"')
    elif kernel_name == 'conda':
        output,errors = __runs(ssh_client,f'docker exec {infos["container"]} /bin/bash -c "/opt/conda/bin/python /root/temp.py"')
    # 关闭SSH连接
    ssh_client.close()

    if errors:
        raise Exception(errors)
    else:
        print(output)


@register_cell_magic
def test(line,cell):
    print(line,'line',type(line))
    print(cell,'cell',type(cell))

# 为了能够在IPython中使用这个魔法命令，需要加载这个扩展
def load_ipython_extension(ipython):
    ipython.register_magic_function(test, 'cell', 'test')
    ipython.register_magic_function(nodeold, 'cell', 'nodeold')
    ipython.register_magic_function(node, 'cell', 'tknode')
    