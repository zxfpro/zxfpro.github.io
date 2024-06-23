(/opt/conda/bin/pip install $1 --no-cache-dir -i http://192.168.8.125:8100/simple/ --trusted-host 192.168.8.125
) || (echo "本地源缺少该包 使用清华源进行下载";
      /opt/conda/bin/pip install $1 --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple/;
      echo "同步到本地源";
      sshpass -p qe1234 pip2pi qe@192.168.8.125:/qe/data/data/pypi/package $1;)
