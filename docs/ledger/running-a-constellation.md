Details on how to run a ledger node are <a href="../../getting-started/run-a-node/" target=_blank>here</a>.

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