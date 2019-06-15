# Quickstart: Building the Fetch.AI components

In this tutorial we will build the full Fetch.AI system. At the present, the ledger and the open economic framework (OEF) needs to be built and deployed invidually. This will change as we approach main net by the end of the year.


## Supported platforms
Currently, we officially support:

- MacOS Darwin 10.13x and higher (64bit)
- Ubuntu 18.04 (x86_64)

We plan to support all major platforms in the future. 

## Building the ledger


### Installing dependencies
The Fetch ledger only depends on CMake, OpenSSL and ASIO. Optionally, it depends on the Python development libraries if you want to build the Python bindings. There currently is an additional dependency which will be removed over time, namely libpng. This dependency only needs to be installed on Ubuntu, but not OS X. ASIO is checked out as a submodule and hence, you do not need to install anything. For OpenSSL and CMake do following on Mac:
```
$ sudo brew install cmake openssl
```
Alternativly if you are using MacPorts:
```
$ sudo port install cmake openssl
```
On Ubuntu / Debian:
```
$ sudo apt-get install libssl-dev cmake python3-dev clang
```

### Download
The Fetch ledger is kept in the repository https://github.com/fetchai/ledger.git. First thing to do, is to checkout the repository:
```
$ cd [working_directory]
$ git clone https://github.com/fetchai/ledger.git
```
Next initialise submodules:
```
$ cd fetch-ledger
$ git submodule update --init --recursive
```

### Building
Assuming that you are in the Fetch ledger repository, you need to do following to build the library:
```
$ mkdir build
$ cd build
$ cmake ..
$ make -j constellation
```
If you use Brew as your package manager on OS X, before building the code you will need to define the location for cmake to find the openssl libraries. An example is shown below. It is recommened that you add this to `~/.bash_profiles` or similar configuration file.
```
$ export OPENSSL_ROOT_DIR=/usr/local/Cellar/openssl/1.0.2o_2
```
Users can interactively configure the build by executing the following command inside the build directory to the project:
```
$ ccmake .
```
For parts of this tutorial you may want to use the Etch simulator `vm-lang`. To build this target write
```
make -j vm-lang
```
in the build folder.

### Running local test node
To run a local node, navigate to the constellation app folder:
```
cd apps/constellation
```
Then start a standalone test node:
```
./apps/constellation/constellation -port 8100 -block-interval 3000 -standalone
```
You should see output similar to following
```
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
Once you see the message
```
[ 2019-06-15 15:24:39.383, # 1 INFO  :                          P2PService ] CORE URI: tcp://127.0.0.1:8101
[ 2019-06-15 15:24:39.383, # 1 INFO  :                          P2PService ] Num Initial Peers: 0
[ 2019-06-15 15:24:39.383, # 1 INFO  :                          P2PService ] Starting P2PService...
[ 2019-06-15 15:24:39.484, # 5 INFO  :                          HTTPServer ] Starting HTTPServer on http://127.0.0.1:8100
[ 2019-06-15 15:24:39.524, # 6 WARN  :       NewVersionedRandomAccessStack ] Attempted to find if hash exists, but history is empty!
[ 2019-06-15 15:24:39.524, # 6 WARN  :       NewVersionedRandomAccessStack ] Attempted to find if hash exists, but history is empty!
[ 2019-06-15 15:24:39.525, # 7 INFO  :                    BlockCoordinator ] Chain Sync complete on 0x780bbb1c050cd3d5c20fce89fa6f4e61c884315efeb44c54ceb956a50563683a (block: 0 prev: 0xd3efbefbefbefbefbefbefbefbe19e9deb22b3efbefbefbefbefbefbefbefbed)
[ 2019-06-15 15:24:40.487, # 1 INFO  :                       constellation ] Startup complete
```
you are ready to start exploring the ledger functionality as we will do in the next tutorial.

### Installing Python API
We download and install the Python library that will allow us to interact with the running node ledger:
```
git clone git@github.com:fetchai/ledger-api-py.git -b release/v0.4.x
```
Make sure you are on the latest release branch in order to have all the latest features. Install the library with the following command:
```
python3 setup.py install
```
We will discuss how to use this API in the part of this documentation.

### Connecting to testnet
Connecting and joining the test net is relatively straight forward. Navigate to the constellation application folder:
```
cd apps/constellation
```
Optionally delete the database files (in the case where you have been running a local network)
```
rm -f *.db
```
Start the network connecting to the alpha test network.
```
./constellation -bootstrap -network alpha
```

## Open economic framework
In order to start a open economic framework (OEF) core running you will need to install docker. You can then start a core by pulling and launching our published image:
```

docker pull fetchai/oef-search:latest

curl http://etch-docs.fetch.ai/oef/assets/node_config.json \
  --output node_config.json

docker run -it -v `pwd`:/config \
  -p 20000:20000 -p 10000:10000 \
  -p 40000:40000 -p 7500 \
  fetchai/oef-search:latest \
  node no_sh --config_file /config/node_config.json
```

A successful run will start producing stats dumps after a few seconds. You will need to have several ports available on your machine — 10000, 20000, 30000 and 7500 — the core may not start properly if something else is running on them.

### Installing the OEF SDK
To install the OEF Python SDK use the Python package manager:
```
pip3 install -v -v -v --no-cache-dir oef
```
You can now start developing agents using the SDK. The first step is to important the agents SDK:
```
from oef import agents
```
When a function needs a core address you should use 127.0.0.1 and port 10000.

### Getting the example code
Later, we will go through an example of an agent in more detail, but get quickly started, you can download the examples here:
```
curl http://etch-docs.fetch.ai/oef/assets/examples.tgz \
  --output examples.tgz
```
