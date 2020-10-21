# CLI - Introduction

The command line client is quite powerful for interacting with the ledger. It is therefore a useful tool to learn how to use.

## Connecting to a network

While some users will want to connect a node to the network and sync the entire blockchain, for many however, it is quicker and easier to connect directly to existing publically available nodes.

### Connecting to Agent Land network

To connect to the agent land network run the following configuration steps:

```bash
wasmcli config chain-id agent-land
wasmcli config trust-node false
wasmcli config node https://rpc-agent-land.fetch.ai:443
```

### Connecting to Agent Land network

To connect to the agent world network run the following configuration steps:

```bash
wasmcli config chain-id agentworld-1
wasmcli config trust-node false
wasmcli config node https://rpc-agentworld.prod.fetch-ai.com:443
```

Checkout the [Network Information](../networks/) page for more detailed information on the available test networks.
