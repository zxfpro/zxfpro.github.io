# 华为生态


## 硬件设备

### 安装NPU:

1 驱动
2 固件
3 MCU
4 Toolkit

### 华为机器的准备
1 调研
docker 支持到多少版本?   
18 版本以上


## 软件

### MindSpore 
[](/Users/zhaoxuefeng/Documents/GitHub/qe_gitee/docs/imgs/1.png)

MindSpore 是一个深度学习框架 MindFormers 是它的一个子项目 即 MindSpore Transformers. 它是专门用于构建一个大模型的训练,推理,部署的全流程套件



### MindStudio
一种集成开发环境 IDE 
NPU 类上的功能强大, 迁移工具 

### MindX DL or MindX SDK
是一种基于昇腾的训练的东西 均运行在K8s 框架上 平台级别的功能

### MindFromers


























## 资料准备
pytorch  
https://repo.huaweicloud.com/kunpeng/archive/Ascend/PyTorch/
 
pytorch npu   
https://gitee.com/ascend/pytorch/releases 

稳定支持到1.11   
这就是在线推理模式，可能会有算子问题。   
推荐用离线推理模式，迁移过程有详细的文档，工作量不大   
离线推理性能比在线推理好   


在线推理模式和离线推理模式是两种不同的机器学习推理策略，   
它们的区别主要在于模型的加载和执行方式。   
在线推理模式是指在AI框架内执行推理的场景，   
例如在Tensorflow框架上，加载模型后，通过session.run执行推理任务。   
相比于离线推理场景，使用在线推理可以方便将原来基于Tensorflow框架做推理的应用快速迁移到昇腾AI处理器，
适用于数据中心推理场景。通常使用服务器根据需要进行推理。   
1离线推理模式是指用户使用AI框架训练好的模型，
通过ATC（Ascend Tensor Compiler）将其转换成昇腾AI处理器支持的离线模型，
然后加载并执行离线模型。
模型转换过程中可以实现算子调度的优化、权值数据重排、内存使用优化等。该推理策略的优点为：

模型运行速度更快、
可以使用批量加载模型、可以部署在更小的设备上。   

1: 离线推理和在线推理 - Ascend Data Center Solution V100R020C30 中心推理解决方案概述 01 - 华为

https://support.huawei.com/enterprise/zh/doc/EDOC1100192461/f593ffd9

https://support.huawei.com/enterprise/zh/doc/EDOC1100192461/f593ffd9

在线推理模式
离线推理模式
TensorRT    ATC
Ascend Tensor Compiler

https://www.jianshu.com/p/34a0f34520e7

https://zhuanlan.zhihu.com/p/627523904

https://www.mindspore.cn/










