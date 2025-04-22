# 部署运行流程
## 1. 在开发板上运行
### 1.1. SemiDrive E3650_DEV_KIT开发板烧录运行
- 开发板：
  HaloOS 提供的 rt_demo 工程支持在 SemiDrive E3650_DEV_KIT 开发板硬件上运行,如果开发者需要基于该开发板运行调试,请自行采购 [E3650_DEV_KIT 开发板](https://support.semidrive.com/product/detail/22)
- 程序烧录工具：
  E3650支持多种烧录工具(如Jlink、Trace32等)，开发者需根据实际需求选择并自备工具。
- 程序烧录：
  程序烧录方法请参考[SemiDrive E3650_DEV_KIT 开发板烧录方法]()
  程序调试方法请参考[SemiDrive E3650_DEV_KIT 开发板调试方法]()

### 1.2. Infineon A2G_TC397_5V_TFT开发板烧录运行
- 开发板：
  HaloOS提供的rt_demo工程支持在Infineon KIT_A2G_TC397_5V_TFT开发板硬件上运行，如果开发者需要基于该开发板运行调试，请自行采购[TC397开发板链接](https://www.infineon.com/cms/en/product/evaluation-boards/kit_a2g_tc397_5v_tft/)
- 程序烧录工具：
  TC397程序烧录支持多种工具，本文档仅描述Infineon官方提供的[Aurix Flasher工具](https://softwaretools.infineon.com/tools/com.ifx.tb.tool.aurixflashersoftwaretool)
  Aurix Flasher工具支持通过串口或DAP/JTAG下载程序，详细的烧录方式说明请参考开发板的User Manual，请在TC397开发板链接页面下载
  如果通过DAP或JTAG接口下载程序，需要采购Infineon提供的[miniwiggler工具](https://www.infineon.com/cms/en/product/evaluation-boards/kit_dap_miniwiggler_usb/)
- 程序烧录：
  Aurix Flasher工具使用请参考工具的帮助文档
  在Aurix Flasher工具中加载`output`目录下编译生成的elf文件，并执行program；烧录完成后请断开连接并进行断电，再重新上电即可正常运行。此时，通过串口连接开发板，可查看运行日志并进行 Shell 命令交互

## 2. 在模拟器上运行（无需硬件）
### 2.1. 快速运行
VCOS SIM（模拟器）提供了一种无需目标硬件平台，可直接在Ubuntu环境上运行配置好的Docker镜像进行仿真调试。目前使用模拟器可以测试VCOS的许多特性，包括调度表，中断，以太通信等
#### 2.1.1. 环境准备
##### 2.1.1.1. 安装linux-gnu-gcc编译器
> 注意：VCOS SIM 强依赖linux-gnu-gcc编译器，Ubuntu下通常有自带的linux-gnu-gcc，如果没有安装，需要执行以下命令安装

```bash
sudo apt update
sudo apt install gcc
```
可以通过`gcc --version`验证安装，如果输出版本号表示安装成功

##### 2.1.1.2. Docker环境部署
下载[vcos_sim Docker镜像](https://gitee.com/yanxiaoyong_1/sim-docker)，解压`vcos_sim.tar.7z.001`得到`vcos_sim.tar`
1. 导入Docker镜像的tar包
   ```bash
   docker load -i vcos_sim.tar
   ```
2. 启动vcos_sim Docker容器，Docker与Ubuntu系统共享目录，方便直接调试
   ```bash
   docker run -it --cap-add=NET_ADMIN --device=/dev/net/tun --name vcos_sim -v /home:/home vcos_sim /bin/bash &
   ```
3. 检查容器是否成功启动
   ```bash
   docker ps -a
   ```
   执行以上命令，可以在进程中看到vcos_sim

4. 进入vcos_sim镜像
   ```bash
   docker exec -it vcos_sim /bin/bash
   ```
5. vcos_sim镜像成功启动以后，可以在Linux系统的vscode中安装Docker和Dev Containers插件  
6. 在vscode中通过安装的插件连接vcos_sim容器，即可在vscode中进行调试  
![vscode连接vcos_sim](../_static/image/quick_start/vscode-connect-docker.png)
7. 在vscode中打开haloosspace文件夹

#### 2.1.2. 在linux系统中执行编译
在[工程编译](./02_compiling.md)章节，已经详细介绍了如何完成编译，支持在开发板上运行。rt_demo运行在VCOS SIM虚拟仿真环境上，需要切换到`haloosspace/vcos/build`目录，执行以下命令编译生成镜像文件：
```bash
python vcos_build.py -app_name rt_demo -board_name E3650_DEV_KIT -compiler gcc -maketool ninja -sim 1 -all
```

#### 2.1.3. 运行
##### 2.1.3.1. 在vcos_sim Docker环境中直接运行
```bash
cd ./output/rt_demo_E3650_DEV_KIT_gcc
./rt_demo
```

##### 2.1.3.2. 在vscode中通过GDB调试
1. 安装 c/c++ 插件
2. 配置launch.json，参考下方示例
    ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "(gdb) 启动",
                "type": "cppdbg",
                "request": "launch",
                "program": "${workspaceFolder}/output/rt_demo_E3650_DEV_KIT_gcc/rt_demo",
                "args": [],
                "stopAtEntry": false,
                "cwd": "${workspaceFolder}",
                "environment": [],
                "externalConsole": false,
                "MIMode": "gdb",
                "setupCommands": [
                    {
                        "description": "为 gdb 启用整齐打印",
                        "text": "-enable-pretty-printing",
                        "ignoreFailures": true
                    },
                    {
                        "description": "Ignore SIGUSR1",
                        "text": "handle SIGUSR1 nostop noprint pass",
                        "ignoreFailures": true
                    }
                ]
            },
        ]
    }
    ```
3. 在vscode中可以直接通过GDB调试运行
