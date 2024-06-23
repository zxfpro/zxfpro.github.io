import paramiko
from scp import SCPClient
import fire
import os

# 远程服务器的IP地址、用户名和密码
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
host_struct = load_json('/packages/host_config.json') #8840

def sync_pip(package = 'rdt',pip_type='pipbase'):
    if pip_type == 'pipbase':
        pips = 'pip_install'
    elif pip_type == 'pip310':
        pips = 'pip310_install'

    if os.system(f'{pips} {package}'):
        return 'error'
    # 这里更改为支持多机,每台机器上支持多容器的同步模式
    # 重新定义数据结构

    def sync_lower_node(host,username,password,container,package):
        print('开始同步到从机\n')
        # 创建SSH客户端并连接到服务器
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, username=username, password=password)
        # 执行远程Python脚本的命令
        command = f'docker exec {container} /bin/bash -c "{pips} {package}"'

        # 通过SSH连接发送命令
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # 获取命令执行的输出和错误
        output = stdout.read().decode()
        errors = stderr.read().decode()

        # 关闭SSH连接
        ssh_client.close()
        # 打印
        print('从机同步完毕\n')
        if errors:
            return errors
        else:
            print(output)

    for node in host_struct:
        for container in node['containers']:
            sync_lower_node(host = node['host'],username = node['username'],password =node['password'],container=container,package=package)



if __name__ == '__main__':
    fire.Fire(sync_pip)
