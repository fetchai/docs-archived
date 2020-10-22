## Local node

From the `build` folder, navigate to the constellation app folder:
``` bash
cd apps/constellation
```


Create a `genesis_file.json`:

Create a file saved as `genesis_file.json` and is saved in the constellation root dir, paste in the below code:

```
{
  "version": 4,
  "accounts": [
    {
      "address": "Your base64 address",
      "balance": 1152997575,
      "stake": 0
    }
  ]
}
```


Start a standalone test node:
``` bash
./constellation -block-interval 4000 -standalone -genesis-file-location genesis_file.json

```
You should see output like this:
``` bash
■ ■ ■ .
■ ■ . .
■ . . .
. . . .
Constellation v1.1.0-alpha19-8-g4cd13f999
Copyright 2018-2019 (c) Fetch AI Ltd.

[I] 2020/01/10 10:01:19 | main                           : Configuration:
lanes................: 1
slices...............: 500
block-interval.......: 4000
standalone...........: Yes
private-network......: No
db-prefix............: node_storage
port.................: 8000
peers................:
external.............: 127.0.0.1
config...............:
max-peers............: 3
transient-peers......: 1
peers-update-cycle-ms: 0
disable-signing......: No
kademlia-routing.....: Yes
bootstrap............: No
discoverable.........: No
host-name............:
network..............:
token................:
processor-threads....: 12
verifier-threads.....: 12
executors............: 1
genesis-file-location: genesis_file.json
experimental.........:
pos..................: No
max-cabinet-size.....: 10
stake-delay-period...: 5
aeon-period..........: 25
graceful-failure.....: No
fault-tolerant.......: No
enable-agents........: No
messenger-port.......: 9010
-
Network Mode.........: Standalone
Num Lanes............: 1
Num Slices...........: 500
Num Executors........: 1
DB Prefix............: 1
Processor Threads....: 12
Verification Threads.: 12
Max Peers............: 3
Transient Peers......: 1
Block Internal.......: 4000ms
Max Cabinet Size.....: 10
Stake Delay Period...: 5
Aeon Period..........: 25
Kad Routing..........: 1
Proof of Stake.......: 0
Agents...............: 0
Messenger Port.......: 9010
Mailbox Port.........: 0
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
./constellation -bootstrap -network testnet
```


## Compiler flags

The following compiler flags run the constellation in various modes.

* `-lanes`: how many lanes to use.
* `-slices`: how many slices to use.                   
* `-block-interval`: block interval in milliseconds.
* `-standalone`: signal the network to run in standalone mode.
* `-private-network`: signal the network to run as part of a private network.
* `-db-prefix`: database prefix.             
* `-port`: starting port for ledger services.
* `-peers`: comma separated list of addresses for initial connection.
* `-external`: global IP address or hostname for the node.
* `-config`: path to the manifest configuration.
* `-max-peers`: maximum number of peers to connect to.
* `-transient-peers`: random number of peers given in answer to peer requests.
* `-peers-update-cycle-ms`: speed of peer updates in milliseconds.
* `-disable-signing`: disable signing of all network messages.
* `-bootstrap`: signal to connect to the bootstrap server.
* `-discoverable`: signal that node can be advertised on the bootstrap server.
* `-host-name`: hostname or identifier for the node.
* `-network`: name of the bootstrap network to connect to.
* `-token`: the authentication token to talk to bootstrap.
* `-processor-threads`: number of processor threads.
* `-verifier-threads`: number of verifier threads.
* `-executors`: number of transaction executors.
* `-experimental`: comma separated list of experimental features to enable.


<br/>
