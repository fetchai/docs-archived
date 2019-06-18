# Building the Fetch.AI components

Currently, the Fetch.AI ledger and the open economic framework (OEF) are built and deployed invidually. This will change with the main net deployment towards the end of the year.


## Supported platforms

- MacOS Darwin 10.13x and higher (64bit)
- Ubuntu 18.04 (x86_64)
- Fetch.AI will eventually support all platforms.


## Building the ledger


### MacOS

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

To avoid issues with OpenSSL, run the following:

``` bash
cmake -DOPENSSL_ROOT_DIR=/usr/local/ssl -DOPENSSL_LIBRARIES=/usr/local/ssl/lib
```


### Ubuntu 

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

There is currently an additional dependency which will be removed over time, namely `libpng`. 


### Redhat - not supported

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


### Download

If you need them, here are the <a href="https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent" target=_blank>Git SSH key generation instructions.</a>

Clone the repository:

``` bash
cd [working_directory]
git clone https://github.com/fetchai/ledger.git
git checkout release/v0.4.x
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


### Building

From the `ledger` directory, follow the steps to build the library:

``` bash
mkdir build
cd build
cmake ..
make -j constellation
```

If you have memory issues on `make`, limit the number of cores:

``` bash
make -j 4 constellation
```

If you want, you can build all the libraries:
``` bash
make -j
```

For the `etch` simulator, build the `vm-lang` library:
``` bash
make -j vm-lang
```


### Run a local node

Go to the constellation app folder:
``` bash
cd apps/constellation
```

Start a standalone test node:
``` bash
./constellation -port 8100 -block-interval 3000 -standalone
```
You should see output like this:
``` bash
F E ╱     Constellation v0.4.1-rc1
   T C     Copyright 2018-2019 (c) Fetch AI Ltd.
     H

[ 2019-06-03 16:55:20.215, # 1 INFO  :                                main ] Configuration:

port......................: 8100
network mode..............: Standalone
num executors.............: 1
num lanes.................: 1
num slices................: 500
bootstrap.................: 0
discoverable..............: 0
host name.................:
external address..........: 127.0.0.1
db-prefix.................: node_storage
interface.................: 127.0.0.1
mining....................: Yes
tx processor threads......: 12
shard verification threads: 12
block interval............: 3000ms
max peers.................: 3
peers update cycle........: 0ms
peers.....................:
manifest.......:
 - HTTP/0: tcp://127.0.0.1:8100 (8100)
 - CORE/0: tcp://127.0.0.1:8101 (8101)
 - Lane/0: tcp://127.0.0.1:8110 (8110)
```

Once you see the message:

``` bash
[ 2019-06-15 15:24:39.383, # 1 INFO  :                          P2PService ] CORE URI: tcp://127.0.0.1:8101
[ 2019-06-15 15:24:39.383, # 1 INFO  :                          P2PService ] Num Initial Peers: 0
[ 2019-06-15 15:24:39.383, # 1 INFO  :                          P2PService ] Starting P2PService...
[ 2019-06-15 15:24:39.484, # 5 INFO  :                          HTTPServer ] Starting HTTPServer on http://127.0.0.1:8100
[ 2019-06-15 15:24:39.524, # 6 WARN  :       NewVersionedRandomAccessStack ] Attempted to find if hash exists, but history is empty!
[ 2019-06-15 15:24:39.524, # 6 WARN  :       NewVersionedRandomAccessStack ] Attempted to find if hash exists, but history is empty!
[ 2019-06-15 15:24:39.525, # 7 INFO  :                    BlockCoordinator ] Chain Sync complete on 0x780bbb1c050cd3d5c20fce89fa6f4e61c884315efeb44c54ceb956a50563683a (block: 0 prev: 0xd3efbefbefbefbefbefbefbefbe19e9deb22b3efbefbefbefbefbefbefbefbed)
[ 2019-06-15 15:24:40.487, # 1 INFO  :                       constellation ] Startup complete
```
you are ready to start exploring the ledger functionality.


### Install the Python API

Download and install the Python library which interacts with the running ledger node:

``` bash
git clone git@github.com:fetchai/ledger-api-py.git -b release/v0.4.x
```

Make sure you are on the latest release branch in order to have the latest features. 

Install the library with the following command:

``` python
cd ledger-api-py/
python3 setup.py install
```

Find out how to build a smart contract using the Python API [here](submitting_contract.md).

<!--### Connecting to testnet

Navigate to the constellation application folder:

``` bash
cd apps/constellation
```

If you have been running a local network, delete the database files:

``` bash
rm -f *.db
```

Start the network connecting to the alpha test network.

``` bash
./constellation -bootstrap -network 
./constellation -bootstrap -network delta
```
-->

## Open economic framework

First, get <a href="https://www.docker.com/get-started">Docker</a>.

Next, pull our published image.

``` bash
docker pull fetchai/oef-search:latest
```
Grab the configuration file.

``` bash
curl https://docs.fetch.ai/oef/assets/node_config.json \
  --output node_config.json
```

And run the Docker image with the configuration.

``` bash
docker run -it -v `pwd`:/config -p 20000:20000 -p 10000:10000 -p 40000:40000 -p 7500 fetchai/oef-search:latest node no_sh --config_file /config/node_config.json
```

A successful run will start producing stats dumps after a few seconds. 

You'll need to have several ports available on your machine: `10000`, `20000`, `30000`, and `7500`.


### Install the OEF SDK

First, run the pip installation command:

``` bash
pip3 install -v -v -v --no-cache-dir oef
```

After that, let's check we installed the SDK correctly:

``` bash
python3
from oef import agents
```

When a function needs a core address, use `127.0.0.1` and port `10000`.


### Getting the example code

Download the <a href="/oef/assets/examples.tgz" download="">working examples bundle</a>.

Or curl them here:

``` bash
curl http://etch-docs.fetch.ai/oef/assets/examples.tgz \
  --output examples.tgz
```

<br/>
