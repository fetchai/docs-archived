## Local node

From the `build` folder, navigate to the constellation app folder:
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

When you see the following message...

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
...your node is running and you will be able to test smart contracts and autonomous agents.


## Connect to a node on testnet
From the same `build/apps/constellation` folder, run the following.
``` c++
./constellation -bootstrap -network alpha
```

## More info

Navigate through to <a href="../../oef" target=_blank>OEF</a>, <a href="../../etch-language/getstarted" target=_blank>`etch` language</a>, <a href="../../smart-contracts/executing-smart-contract-code/" target=_blank>smart contracts</a>, and <a href="../../tutorials/submitting_contract" target=_blank>tutorials</a> links where you will find instructions and tutorials.


<br/>