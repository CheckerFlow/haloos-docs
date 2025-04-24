# Project Compilation
## 1. Compilation environment preparation
### 1.1 Installing VCOS Studio Configuration Tool Dependency Plugin
#### 1.1.1. Windows System
1. Open PowerShell with [Administrator Permissions] and under the root directory `haloosspace`
2. Execute the following command
```bash
python ./vcos/vcos_studio/configurator/init_env.py -a
```
#### 1.1.2. Linux system
1. Open the Linux terminal and under the root directory `haloosspace`
2. Execute the following command
```bash
sudo apt update
sudo apt install python3.8-venv libxcb-cursor0
python ./vcos/vcos_studio/configurator/init_env.py -a
```
> If Python 3.8-venv cannot be found in higher versions of Ubuntu, run `sudo add-apt-repository ppa:deadsnakes/ppa` to add the deadsnakes PPA source (used to provide older versions of Python), and then run the above command again
### 1.2. Install the compilation toolchain
In the `haloosspace` directory, execute the following command to install the compilation toolchain:
```bash
python ./vcos/build/compiling_env.py
```
This command performs the following installation steps in turn:
- Install CMake tools and add the installation path to the PATH environment variable
- Install kconfiglib tool
- Install make tool and set the `NINJA_TOOL_PATH` environment variable
- Install ninja tools and set `NINJA_TOOL_PATH` environment variable
- Install tricore-gcc compile toolchain and add the installation path to the PATH environment variable
- Install arm-gcc compile toolchain and add the installation path to the PATH environment variable
- Install Docker Tools

## 2. Compilation
### 2.1. One-click compilation

> Windows system needs to open PowerShell with [Administrator Permissions] and switch to the `haloosspace` directory

- Switch to the `haloosspace/build` directory:
```bash
cd ./build
```
- Compile rt_demo application: configure the E3650_DEV_KIT board-level configuration, use the gcc compiler, use make as make tool, and supports running on the actual development board hardware
```bash
python haloos_build.py -app_name rt_demo
```

This command will complete the following operations in turn:

- Generate dynamic code based on E3650_DEV_KIT board-level configuration of rt_demo application
- Automatic construction through CMake call make tool
- Final compilation to generate image files
- The compiled product is saved by default in the `haloosspace/output/rt_demo_E3650_DEV_KIT_gcc` directory

> To compile vbslite_demo, replace -app_name rt_demo in the above command with -app_name vbslite_demo

### 2.2. Compilation instructions
For detailed compilation command instructions, please refer to [HaloOS Compilation Framework Description] (https://gitee.com/haloos/build/blob/master/README.md)

If you modify the code or add a new code directory and modify the CMakeLists.txt file, you need to delete the corresponding output directory and re-execute the compilation command

```bash
rm -r ./output # Delete the output directory
python haloos_build.py -app_name rt_demo # Recompile
```