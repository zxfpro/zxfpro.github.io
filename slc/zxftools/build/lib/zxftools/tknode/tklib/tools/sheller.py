import subprocess
import os
class EnvBase():
    """
    work,works方法二：先用 os.chdir 切换工作目录，
    再用 os.system 执行命令，例如：os.chdir("path-to-repo")
    os.system("python setup.py install")13。
    """
    def __init__(self):
        self.cwd = None

    def work(self, order, run=False):
        if run:
            if order.startswith('cd'):
                cwd = order.split(' ')[-1]

                os.chdir(cwd)
                print(os.getcwd())

                self.cwd = os.getcwd()
                return 'success'
            out, err, return_code = self._execute_shell_command(order, cwd=self.cwd)
            if return_code == 0:
                return out or 'success'
            else:
                return f"Error {out}"
        else:
            return order

    def works(self, orders, run=False):
        if run:
            order_result = []
            for order in orders:
                result = self.work(order, run)
                order_result.append(result[-100:])

            return '\n'.join(order_result)

        else:
            return orders

    def _execute_shell_command(self, cmd, cwd=None):
        # 创建一个子进程来执行shell命令
        process = subprocess.Popen(cmd, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # 获取命令的输出和错误信息
        out, err = process.communicate()
        # 获取命令的返回码
        return_code = process.returncode
        # 返回命令的输出、错误信息和返回码
        return out.decode(), err, return_code

    def word_count(self,text: str) -> str:
        """the tool use to know the number of word"""
        return len(text)

import paramiko
import time
from .base import BaseTools
from zxftools.logger import Logger

class ShellTools(BaseTools):
    register_default = ['vim_open', 'vim_write', 'localhost_terminal',
                        'remotehost_terminal', 'remotehost_logout', 'remotehost_login']
    def __init__(self,human_supervision=True, register=[],log_path = '~/.zxf_file/cache/ai_shell.log'):

        super().__init__(register,self.register_default)
        self.logger = Logger(log_path)
        self.ssh = None
        self.channel = None
        self.human_supervision = human_supervision
        self.env = EnvBase()

    def _guard(self,command:str)->None:
        for order in ['rm ','mv ','ln ']:
            if order in command:
                k = input(f'ask for : {command}  y/n')
                if k == 'n':
                    raise "退出"
        if self.human_supervision:
            k = input(f'ask for : {command}  y/n')
            if k == 'n':
                raise "退出"

    def _get_result(self,interval=1):
        result_all = ''
        while True:
            time.sleep(interval)
            if self.channel.recv_ready():
                output = self.channel.recv(65535)  # 读取数据
                result = output.decode('utf-8')
                result_all += result
            else:
                break
        return result_all

    def vim_open(self,file:str)->str:
        """
        Tools that mimic vim can open files and view their contents
        """
        self._guard(file)
        with open(file,'r') as f:
            content = f.read()
        return content
    def vim_write(self,content:str,file:str)->str:
        """
        Tools that mimic vim can overwrite new content to a specified file
        """
        k = input(f'{content} want to write : {file}  y/n')
        if k == 'n':
            raise "退出"
        with open(file,'w') as f:
            f.write(content)
        return 'write success'

    def localhost_terminal(self,shell_command: str) -> str:
        """
        A tool can manipulate the local terminal with continuous multistep
        """
        self._guard(shell_command)
        if not shell_command.startswith('rm'):

            self._guard(shell_command)
            self.logger.info(f"localhost: {shell_command}")
            shell_commands = shell_command.split('&&')

            commands = [i.strip() for i in shell_commands]
            end = self.env.works(commands, run=True)
            return end

            # if len(commands) > 1:
            #     end = self.env.works(shell_command, run=True)
            #     return end
            # if shell_command
            #
            # end = self.env.work(shell_command, run=True)
            # return end
        else:
            return "you can not to use rm order"

    # TODO 尽可能避免异步命令
    def remotehost_terminal(self,shell_command: str) -> str:
        """
        the tool to use remote server terminal
        """
        self._guard(shell_command)

        self.logger.info(f"remotehost: {shell_command}")
        # 发送命令
        self.channel.send(f'{shell_command}\n')
        result = self._get_result(1)

        if len(result)>1000:
            result_all = result[:500] + '......' + result[-500:]
        else:
            result_all = result

        # # 等待命令执行
        # time.sleep(wait_time)

        # 获取结果
        # while not self.channel.recv_ready():  # 等待直到有数据可以接收
        #     time.sleep(1)
        #
        # output = self.channel.recv(65535)  # 读取数据
        return result_all

    def remotehost_logout(self) -> str:
        """
        the tool logout remote server
        """
        # 关闭通道
        self.channel.close()
        # global ssh
        self.ssh.close()

        return "logout success"

    def remotehost_login(self,ip: str, username: str, password: str) -> str:
        """
        the tool to login remote server
        """
        # 创建SSH对象 #TODO 不安全
        self.ssh = paramiko.SSHClient()
        # 自动接受不在known_hosts文件的主机密钥
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # 连接服务器
        self.ssh.connect(ip, port=22, username=username, password=password)
        # 创建一个交互式的shell会话
        trans = self.ssh.get_transport()
        self.channel = trans.open_channel("session")
        self.channel.get_pty()
        self.channel.invoke_shell()

        # 等待通道准备好
        time.sleep(1)
        return "login success"




'''
case "$1" in
  -h|--help)
    pip cache dir  # 显示缓存的目录
    pip cache list  # 显示缓存目录中的所有文件
    pip cache purge # 清除缓存目录中的所有文件
    pip freeze > requirements.txt  # 环境导出
参数配置
    pip config set global.index-url http://{url}/simple/
    pip config set global.trusted-host {url}
安装
    pip install {package} --no-cache-dir -i http://192.168.8.125:8100/simple/ --trusted-host 192.168.8.125
    pip install -r requirements.txt
    pip download {package} -d {path}
pip2pi
    pip2pi {home_path} {package}
    pip2pi {home_path} -r requirements.txt
"""
echo "conda 操作"
echo """
    conda create -n {name} python={python}
    conda env create -f environment.yml
    conda create --name {name} --clone {origin}
    conda —c {channel} install {package}
    conda config --set show_channel_urls yes 显示conda配置中的通道URL。 设置搜索时显示通道地址
    conda config --remove-key channels
    conda config --add channels {url}
    conda config --remove channels {url}
    conda install --revision N：这个命令可以让你恢复到之前的某个版本，N是版本号，你可以用conda list --revisions查看。
    conda list --revisions：这个命令可以列出你安装或卸载的所有包的历史记录，每次改变都有一个版本号和时间戳。
    conda list -n env_name -r：这个命令可以列出某个环境下的所有包的历史记录，env_name是环境的名字，你可以用conda env list查看。
"""
echo "docker 操作"
echo """
    work docker ps
    work docker jupyter
    docker image ls
    docker image rm {imageName}


    docker version
    docker info
    docker login
    docker search {image_name}
    docker logs {container_id}
    docker start {container_id}
    docker stop {container_id}
    docker restart {container_id}
    docker kill {container_id}
    docker rm {container_id}
    docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}"

    sudo usermod -aG docker {username} #将用户添加到docker用户组。
    docker pull {name_version} #从Docker Hub拉取一个镜像。
    docker push {name_version} 将一个镜像推送到Docker Hub。
    docker exec -it {container_id} /bin/bash
    docker commit -m {message} -a "zhaoxuefeng" {container_id} {name_version} 提交一个容器的更改。
    docker build -t {name_version} .

"""
echo "jupyter"

echo """
    jupyter
    jupyter lab password
    jupyter server password
    jupyter lab --generate-config
    jupyter lab --notebook-dir={notebook_dir} --port {port} --root-allow

    pycharm风格设置
    #pycharm 的 File -> Settings -> Plugins,搜索Material Theme UI 并安装,安装之后进行restart
    #02字体:File -> Settings -> Editor -> Font, Font: Source Code Pro,Size: 16, line-spacing: 1.0, apply,保存 .
    #03字体颜色:File -> Settings -> Editor -> Color Scheme Font -> General, scheme选择Darcula, apply,保存 .( 这里我是设置的黑色,如果喜欢白色的可以选择github更佳美观 )
    #04背景图片:设置的路径为:File | Settings | Appearance & Behavior | Appearance选择Background Image
    """

echo "user"
echo """
    #sudo adduser {username}
    #sudo passwd {username}
    #passwd {username}
    """

echo "linux"
echo """
    #ps -ef | grep {progress}
    #lsof -i:{port}
    #kill -9 {pid}
    #tar -zcvf {path}.tar.gz {path}
    #tar -zxvf {tgz_path}
    #zip {files}
    #unzip -O CP936 {files}
    #lspci | grep NVIDIA
    #uname -a 查看Ubuntu版本信息

    #初始化Ubuntu环境
    #sudo apt update
    #sudo apt install build-essential
    #sudo apt install python3.8
    #sudo apt install pciutils
    #
    #ln -s {origin_path} {to_path}
    #wget -c {url}
    #ssh -N -f -L localhost:$1:localhost:$1 root@$2
    #alias {name}='{order}'
    #rsync -avh --progress --partial /path/to/source user@remote:/path/to/destination
    #

#cache缓存替换
#mv ~/.cache /path/to/new/cache
#ln -s /path/to/new/cache ~/.cache
#
#sudo sshfs -o cache=yes,allow_other {target} {a}
#du -sh {file_path}
#sudo mount {a} {b}
#chmod -R 777 {file_path}
#mkdir -p {file_path}
#history {n}
#history -c
## 默认注释了源码镜像以提高 apt update 速度，如有需要可自行取消注释
#deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
## deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy main restricted universe multiverse
#deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
## deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-updates main restricted universe multiverse
#deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
## deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-backports main restricted universe multiverse
#deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
## deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-security main restricted universe multiverse
## 预发布软件源，不建议启用
## deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
## deb-src https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ jammy-proposed main restricted universe multiverse
#>> /etc/apt/sources.list

"""

echo """
## ssh
#    work ssh create root@192.168.8.125
#    work ssh install root@192.168.8.125
    """
    echo """
#tmux ls
#tmux new -s {session_name}
#tmux detach
#tmux attach -t {session_name}
#tmux kill-session -t {session_name}
#tmux switch -t {session_name}
#tmux rename-session -t {session_name} {new_name}
#tmux send-keys -t {session}:{window} "{order}" C-m
#
#        #%：划分左右两个窗格。
#        <arrow key>：光标切换到其他窗格。
#        ;：光标切换到上一个窗格。
#        o：光标切换到下一个窗格。
#        {：当前窗格与上一个窗格交换位置。
#        }：当前窗格与下一个窗格交换位置。
#        Ctrl+o：所有窗格向前移动一个位置，第一个窗格变成最后一个窗格。
#        Alt+o：所有窗格向后移动一个位置，最后一个窗格变成第一个窗格。
#        x：关闭当前窗格。
#        !：将当前窗格拆分为一个独立窗口。
#        z：当前窗格全屏显示，再使用一次会变回原来大小。
#        Ctrl+<arrow key>：按箭头方向调整窗格大小。
#        q：显示窗格编号。

    """
echo """
#    cuda
关闭系统驱动
sudo sh -c \"echo 'blacklist nouveau' > /etc/modprobe.d/blacklist-nouveau.conf\"
sudo sh -c \"echo 'options nouveau modeset=0' >> /etc/modprobe.d/blacklist-nouveau.conf\"
sudo update-initramfs -u
sudo reboot

#    lsmod | grep nouveau 检查是否已经关闭驱动

#    验证安装
#     nvcc -V
      nvidia-smi
      python -c 'import torch;print(torch.cuda.is_available())'
      python -c 'import torch;a = torch.ones(1,2,3,4);print(a.to(0))'

#watch -n 2 -d nvidia-smi 查看gpu状态# 每隔2秒刷新一次，每次只在固定位置刷新
#CUDA_VISIBLE_DEVICES=0 {text}
#!find /qe/data/data -name package
#%cat /sys/class_level/thermal/thermal_zone0/temp
#
#

配置
#
#nvidia-smi No devices were found
#sudo add-apt-repository ppa:graphics-drivers/ppa #不知是否必要
#sudo apt-get install ubuntu-drivers
#ubuntu-drivers devices
#执行结果
#sudo apt install -y nvidia-driver-525
#sudo reboot
#
#\"echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda/lib64'>> ~/.bashrc\"
#\"echo 'export PATH=$PATH:/usr/local/cuda/bin'>> ~/.bashrc\"
#\"echo 'export CUDA_HOME=$CUDA_HOME:/usr/local/cuda'>> ~/.bashrc\"
#source ~/.bashrc
#sudo ldconfig


#   def cudnn(self):
#
#        • sudo dpkg -i cudnn-local-repo-ubuntu2004-8.9.6.50_1.0-1_amd64.deb
#        • sudo cp /var/cudnn-local-repo-ubuntu2004-8.9.6.50_1.0-1_amd64/cudnn-local-4B348671-keyring.gpg /usr/share/keyrings/
#        • sudo apt update
#
#        • sudo apt install libcudnn8
#        • sudo apt install libcudnn8-dev
#        • sudo apt install libcudnn8-samples
#
#        from torch.backends import cudnn
#        assert isinstance(cudnn.version(),int)
#        assert cudnn.is_available() == True
#        a=torch.tensor ( 1.)
#        assert cudnn.is_acceptable (a.cuda ()) ==True
#
#
#    def tensorrt(self):
#
#        sudo dpkg -i tensorrt.deb
#        sudo cp /var/cudnn-local-repo-ubuntu2004-8.9.6.50_1.0-1_amd64/cudnn-local-4B348671-keyring.gpg /usr/share/keyrings/
#        sudo apt update
#        sudo apt install tensorrt

"""


    exit 0
    ;;
  -v|--version)
    echo "1.1.0"
    exit 0
    ;;
  *)
    ;;
esac


# 获取操作类型和文件名
operation=$1
operation2=$2
filename=$3
source_url=$SourceUrl #192.168.8.125:8100
#    -p8890-9000:8890-9000 \
# 根据操作类型和是否快速模式执行相应的命令
if [ "$operation" == "docker" ]; then
    if [ "$operation2" == "ps" ]; then
        docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}" --all
    elif [ "$operation2" == "jupyter" ]; then
        docker run -v /Users/zhaoxuefeng/GitHub:/Users/zhaoxuefeng/GitHub \
                   -v /Users/zhaoxuefeng/Documents:/Users/zhaoxuefeng/Documents \
                   -p8888:8888 \
                   --name=$filename \
                   --rm jupyter:latest
    else
        echo "other"
    fi

elif [ "$operation" == "ssh" ]; then
    if [ "$operation2" == "create" ]; then
      bash /usr/local/bin/tools/ssher.sh create $filename
    elif [ "$operation2" == "install" ]; then
      bash /usr/local/bin/tools/ssher.sh install $filename
    else
	    echo "输入错误"
    fi
else
    echo "Unsupported operation: $operation"
    exit 1
fi





# 获取操作类型和文件名
operation=$1
operation2=$2
filename=$3
source_url=$SourceUrl #192.168.8.125:8100


# 根据操作类型和是否快速模式执行相应的命令
if [ "$operation" == "docker" ]; then
    if [ "$operation2" == "ps" ]; then
        docker ps --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}" --all
    elif [ "$operation2" == "triton_vllm" ]; then
	    docker run --gpus '"device=1"' --shm-size=2g --name "$filename" \
		    -p8000:8000 -p8001:8001 -p8002:8002 \
            -v /qe/data/data/TritonConfigs:/models -w /models \
            -v /qe/data/data/Models_LLM:/llmModels \
		        nvcr.io/nvidia/tritonserver:23.12-vllm-python-py3 tritonserver --model-repository=/models --model-control-mode explicit --load-model demo

    elif [ "$operation2" == "jupyter" ]; then
        docker run -v /Users/zhaoxuefeng/GitHub:/Users/zhaoxuefeng/GitHub \
                   -v /Users/zhaoxuefeng/Documents/:/home \
                   -p8888-9000:8888-9000 \
                   -e computer_username='qe' \
                   -e computer_password='qe1234' \
                   --name='zxf_8888' \
                   --rm jupyter:latest
    elif [ "$operation2" == "project" ]; then
        docker run #TODO
    else
	    echo "输入错误"
    fi

elif [ "$operation" == "package" ]; then
    if [ "$operation2" == "update_private" ]; then
	    bash /usr/local/bin/tools/pip_source.sh private "$filename"

    elif [ "$operation2" == "install_private" ]; then
	    pip install "$filename" -i http://"$source_url"/private/simple/ --trusted-host "$source_url"

    elif [ "$operation2" == "install_cache" ]; then
	    pip install "$filename" -i http://"$source_url"/cache/simple/ --trusted-host "$source_url"
    else
	    echo "输入错误"
    fi

elif [ "$operation" == "conda" ]; then
    if [ "$operation2" == "create_stable" ]; then
	    bash /usr/local/bin/tools/pip_source.sh private "$filename"

    elif [ "$operation2" == "update_stable" ]; then
	    pip install "$filename" -i http://"$source_url"/private/simple/ --trusted-host "$source_url"

    elif [ "$operation2" == "create_test" ]; then
	    pip install "$filename" -i http://"$source_url"/cache/simple/ --trusted-host "$source_url"
    else
	    echo "输入错误"
    fi

else
    echo "输入错误"
    exit 1
fi



'''