#!/bin/bash
# 检测系统架构
ARCH=$(uname -m)
MINICONDA_URL=""
if [ "$ARCH" = "x86_64" ]; then
    # 如果是x86_64架构
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
elif [ "$ARCH" = "aarch64" ]; then
    # 如果是ARM架构
    MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh"
else
    echo "不支持的架构: $ARCH"
    exit 1
fi
# 下载Miniconda安装脚本
wget $MINICONDA_URL -O miniconda.sh

