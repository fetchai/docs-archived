# Installing and building the ledger on Linux Redhat


## Initial setup

Set environment variables:

``` bash
export CC=clang
export CXX=clang++
```

Install dependencies:

``` bash
yum install -y sudo
yum install -y make
yum install -y cmake
yum install -y libpng-devel
yum install -y zlib-devel
yum install -y openssl-devel
yum install -y python36-devel (replace 36 with your version of Python3)
yum install -y clang
yum install -y epel-release (dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm)
yum install -y python-pip (prb. already installed)
yum install -y git 
pip2 install --upgrade pip
pip3 install --upgrade pip
pip install --upgrade cldoc
yum install -y autoconf
yum install -y automake
yum install -y wget
yum install -y which
yum install -y tree

```


## Download the ledger code

If you need them, here are the <a href="https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent" target=_blank>Git SSH key generation instructions.</a>

Clone the repository:

``` bash
cd [working_directory]
git clone https://github.com/fetchai/ledger.git
git checkout release/v0.9.x
```

Update and initialise submodules from the repository root directory:

``` bash
cd ledger
git pull
git submodule update --init --recursive
```

Make sure you have all the submodules:

``` bash
git submodule status
```

If any submodules are missing, please check your installation.


## Build the ledger

From the `ledger` directory, follow the steps to build the library:

``` bash
mkdir build
cd build
cmake ..
make -j constellation
```

You may have memory issues on `make`, so limit the number of cores (we chose 4):

``` bash
make -j 4 constellation
```

If you want, you can build all the libraries:
``` bash
make -j 4
```

For the `etch` simulator, build the `etch` library:
``` bash
make etch
```


<br/>