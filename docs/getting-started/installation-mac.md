# Building the Fetch.AI components

Currently, the Fetch.AI ledger and the open economic framework (OEF) are built and deployed individually. This will change with the main net deployment towards the end of the year.


## Supported platforms

- MacOS Darwin 10.13x and higher (64bit)


## Initial setup

Get homebrew:

``` bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install dependencies:

``` bash
brew install cmake openssl git python
```


Or with MacPorts:

``` bash
port install cmake openssl git python
```

If you use `homebrew`, edit your `~/.bash_profile` :

``` bash
export OPENSSL_ROOT_DIR="/usr/local/Cellar/openssl/`ls /usr/local/Cellar/openssl/ | sort | tail -1`"
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
git checkout release/v0.6.x
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

## Possible gotchas

To avoid issues with OpenSSL, run the following:

``` bash
cmake -DOPENSSL_ROOT_DIR=/usr/local/ssl -DOPENSSL_LIBRARIES=/usr/local/ssl/lib
```



<br/>
