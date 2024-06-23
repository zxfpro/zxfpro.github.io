#!/bin/bash
# 检查参数数量
if [ "$#" -lt 2 ]; then
    echo "Usage: pipbase install [--quick] <filename>"
    exit 1
fi

# 获取操作类型和文件名
operation=$1
quick_mode="false"
filename=""

# 解析参数
for arg in "$@"
do
    case $arg in
        --quick)
            quick_mode="true"
            shift # 移除处理过的参数
            ;;
        *)
            filename=$arg
            ;;
    esac
done

#host = os.environ.get('computer_host','192.168.8.125_126')
# username = os.environ.get('computer_username','qe')
# password = os.environ.get('computer_password','qe1234')
# temp_path = os.environ.get('computer_temp',os.path.join(os.getcwd(),'.computer_temp.py'))
# container = os.environ.get('computer_container',None)
# computer_slave_path = os.environ.get('computer_slave_path','/qe/data/project/project_zxf')

# 根据操作类型和是否快速模式执行相应的命令
if [ "$operation" == "install" ]; then
    if [ "$quick_mode" == "true" ]; then
        echo "Inserting $filename in quick mode"
        # 这里可以放置快速插入的代码
    else
        #echo "Inserting $filename in normal mode"
        # 这里可以放置普通插入的代码
        python /packages/syncpip.py -package $filename -pip_type pipbase
        
    fi
elif [ "$operation" == "uninstall" ]; then
    if [ "$quick_mode" == "true" ]; then
        echo "Inserting ssss $filename in quick mode"
        # 这里可以放置快速插入的代码
    else
        echo "Inserting ssss $filename in normal mode"
        # 这里可以放置普通插入的代码
    fi
else
    echo "Unsupported operation: $operation"
    exit 1
fi

