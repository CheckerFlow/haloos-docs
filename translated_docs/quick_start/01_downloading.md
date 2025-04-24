# Source code download process
## 1. Windows system
> Note that all instructions involving PowerShell in this system are required to be opened through [Administrator Permissions], otherwise the installation may fail
### 1.1. Install Python 3.8.10
> Note: Please use Python 3.8.10, HaloOS's tools rely heavily on this version

1. Download [Python 3.8.10 official installation package](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe) (default is x64 version). Please check "Add to Path" when installing to add it to the environment variables.

> Tip: If there are multiple Python versions in this machine, please switch to version 3.8.10
2. Restart PowerShell, enter `python --version`, and if you output version 3.8.10, it means the installation is successful.
### 1.2. Install git repo tool
Code download depends on both git and git repo. If git is not installed, please [Download and install](https://git-scm.com/downloads/win)

The installation process of git is skipped here. The compilation process also requires the use of git patch tool. Windows system needs to add the patch tool path to the PATH environment variable:
1. Find the installation path where git is located, and add \usr\bin is the path where patch.exe is located (for example: C:\Program Files\Git\usr\bin)
2. Press Win + S to search for "Environment Variables" → select "Edit System Environment Variables"
3. Find Path in "User Variables" → Click "Edit" → "New" → Add the above patch path → Save
4. Restart PowerShell with administrator permissions, execute `patch --version`, and output the version number to indicate successful installation

The installation process of git repo is as follows:
1. Download [git repo official compression package] (https://git-repo.info/releases/v0.7.8/git-repo-0.7.8-Windows-64.zip) and decompress
2. Copy the unzipped git-repo.exe to the git installation directory cmd path (such as C:\Program Files\Git\cmd, note that this path has been added to the environment variables when installing git. If it is not added, you need to perform the following steps 3~5)
3. Press Win + S to search for "Environment Variables" → select "Edit System Environment Variables"
4. Find Path in "User Variables" → Click "Edit" → "New" → Add the above cmd path → Save
5. Restart PowerShell and run the following command. If the version number is displayed, the installation will be successful.
```PowerShell
git --version # version information should be output
git-repo --version # version information should be output
```
### 1.3. Download the code
1. To generate/add ssh key, please press [gitee ssh key addition process] (https://gitee.com/help/articles/4181#article-header0)
2. Configure git
```bash
git config --global user.name "Replace with your name"
git config --global user.email "Replace with your mailbox"
```
3. Switch to the directory where you store the code and run the following script to download the code
> Tip: Here the code is placed in the haloosspace directory

```bash
mkdir haloosspace
cd haloosspace
rm -r ./.repo/ # If there is a synchronization failure before, you need to delete the original .repo directory; if there is no .repo directory, you can ignore this step
git-repo init -u git@gitee.com:haloos/manifests.git -b master -m default.xml
git-repo sync
```
> For more use of git repo, you can enter `git-repo -h` to view

## 2. Linux system (Ubuntu)
### 2.1. Install Python 3.8.10
> Note: Please use Python 3.8.10, HaloOS's tools rely heavily on this version
1. Install the dependency library
```bash
sudo apt update && sudo apt install -y liblzma-dev libbz2-dev libssl-dev build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libreadline-dev libffi-dev libsqlite3-dev
```
2. Run the following command (install and manage Python version through pyenv)
```bash
curl https://pyenv.run | bash
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc
pyenv install 3.8.10
pyenv global 3.8.10
python --version
```
3. If the version number of Python is displayed is 3.8.10, it means the installation is successful.
### 2.2. Install git repo tool
> Ubuntu usually comes with git tools, which can be checked with `git --version`. If it is not installed, you can install it through the `sudo apt install git` command

1. Run the following command to install the repo tool
```bash
curl https://storage.googleapis.com/git-repo-downloads/repo > repo
sudo chmod +x repo
sudo mv repo /usr/bin # Move repo to /usr/bin directory
```
2. Run `repo --version`, and the version number is displayed and the installation is successful.
### 2.3. Download the code
1. To generate/add ssh key, please press [gitee ssh key addition process] (https://gitee.com/help/articles/4181#article-header0)
2. Configure git
```bash
git config --global user.name "Replace with your name"
git config --global user.email "Replace with your mailbox"
```
3. Switch to the directory where you store the code and run the following script to download the code
> Tip: Here the code is placed in the haloosspace directory

```bash
mkdir haloosspace
cd haloosspace
rm -rf ./.repo/ # If there is a synchronization failure before, you need to delete the original .repo directory; if there is no .repo directory, you can ignore this step
repo init -u git@gitee.com:haloos/manifests.git -b master -m default.xml
repo sync
```

> For more use of repo, you can enter `repo -h` to view