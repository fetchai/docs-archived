# Building the Fetch.AI components

Currently, the Fetch.AI ledger and the open economic framework (OEF) are built and deployed invidually. This will change with the main net deployment towards the end of the year.


## Supported platforms

- Ubuntu 18.04 (x86_64)



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

For the `etch` simulator, build the `vm-lang` library:
``` bash
make vm-lang
```


## Run a local node

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



<br/>
