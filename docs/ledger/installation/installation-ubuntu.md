# Installing and building the ledger on Linux Ubuntu

## Initial setup

Set environment variables in `/etc/profile`:

``` bash
export CC=clang
export CXX=clang++
```

Update:

``` bash
sudo apt-get update
```


Install dependencies:

``` bash
apt-get install build-essential clang git cmake libssl-dev doxygen python3-dev python3-pip python3-venv
```

Update:

``` bash
sudo apt-get update
```

Add the git alias:

``` bash
git config --global alias.pullall '!f(){ git pull "$@" && git submodule sync --recursive && git submodule update --init --recursive; }; f'
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
