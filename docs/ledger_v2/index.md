# Getting Ready for Mainnet V2

We are hard at work preparing for Fetch mainnet version 2, which is currently due for release in the next few months. But you can get prepared __now__. This documentation covers some of the things you need to know in order to prepare for and develop for this new network:

- How to connect to the testnets
- The basic resources such as block explorers and token taps
- Python code for creating and funding addresses
- Python code for submitting transactions
- Hardware wallet support
- Roadmap for smart contracts

We have a testnet that is up and running for agent development called Agentland. Agentland is **fully supported** by our Agent Framework from version 0.6 and above. If you are developing autonomous economic agents using our latest framework, then moving to Agentland is relatively straightforward, unless smart contracts are involved. 

## Key links and information

Block explorer and token tap: https://explore-agent-land.fetch.ai/

Understanding building block relationships: https://docs.fetch.ai/aea/oef-ledger/

### Network API, end-points and information

**Chain ID:** agent-land

**Coin denomination:** atestfet

**Decimals:** 18 (i.e. 1 testfet = 10^18 atestfet)

**RPC Endpoint:** [https://rpc-agent-land.fetch.ai:443](https://rpc-agent-land.fetch.ai/)

**Token Faucet:** https://faucet-agent-land.fetch.ai/claim

**REST Endpoit:** [https://rest-agent-land.fetch.ai:443](https://rest-agent-land.fetch.ai/)

You can read more detailed information on [Github](https://github.com/fetchai/networks-agentland). 

## Agentland

Most developers will be interacting with the **Agentland** testnet. This is specifically designed and supported for autonomous economic agent development. There are other testnets, such as those supporting our unique DRB (decentralised random beacon) and other exciting technologies. When we come to the mainnet, all of these testnets will become one: a single network supporting all the new features. 

Agentland and other testnets on the journey have a new address format. Here is a typical example:

```
fetch1almpjpf769p23k0v4m5eglvzr4jupsjs66vxf4
```

**These addresses are not compatible with mainnet v1 or testnet v1.** 

### Other testnets

There are currently three key sequential testnets planned, but more may arise and operate in parallel in order to target the testing and development of specific additional new technologies. The three main incentivised testnet phases are:

1. **Agents**: a stable testnet for autonomous economic agents, featuring the core new mainnet v2 technologies that agent developers need in order to prepare.
2. **Random Beacon**: a stable testnet showcasing the decentralised random beacon, vital for DeFi, gaming and a key part of our on-going unique approach to consensus.
3. **Oracles**: a stable testnet for demonstrating connecting the outside world to the inside world; enabling agents to communicate reliable, trustworthy information from the environment at large. 

## Simple Python using Agentland

In this section, we look at some Python that you can use to create addresses, fund them, and submit transactions to the network. It's super-simple to do:

```python
from aea.crypto.fetchai import FetchAICrypto, FetchAIApi, FetchAIFaucetApi

# Get a new address:
fetch_crypto = FetchAICrypto()
address = fetch_crypto

# This is relatively slow, so if you need to stock up a number of
# addresses, it’s best to get it ONCE, then distribute yourself:
# for rapid tests:
FetchAIFaucetApi().get_wealth(address)
balance = FetchAIApi().get_balance(address)
print(f”Our address {address} has a balance of {balance}”)
```

As you can see, it’s super-easy to use. The above works in standalone code, and is supported in the agent framework. Here is a code fragment that shows the construction, signing and submission of a transaction:

```python
from aea.crypto.fetchai import FetchAICrypto, FetchAIApi, FetchAIFaucetApi

# ... code, etc...

def test_construct_sign_and_submit_transfer_transaction():
    """Test the construction, signing and submitting of a transfer transaction."""
    account = FetchAICrypto()
    balance = get_wealth(account.address)
    assert balance > 0, "Failed to fund account."
    fc2 = FetchAICrypto()
    fetchai_api = FetchAIApi(**FETCHAI_TESTNET_CONFIG)
    amount = 10000
    assert amount < balance, "Not enough funds."
    transfer_transaction = fetchai_api.get_transfer_transaction(
        sender_address=account.address,
        destination_address=fc2.address,
        amount=amount,
        tx_fee=1000,
        tx_nonce="something",
    )
    assert (
        isinstance(transfer_transaction, dict) and len(transfer_transaction) == 6
    ), "Incorrect transfer_transaction constructed."
    signed_transaction = account.sign_transaction(transfer_transaction)
    assert (
        isinstance(signed_transaction, dict)
        and len(signed_transaction["tx"]) == 4
        and isinstance(signed_transaction["tx"]["signatures"], list)
    ), "Incorrect signed_transaction constructed."
    transaction_digest = fetchai_api.send_signed_transaction(signed_transaction)
    assert transaction_digest is not None, "Failed to submit transfer transaction!"

        # Now let's wait around for a while for this transaction to go through"
    not_settled = True
    elapsed_time = 0
    while not_settled and elapsed_time < 20:
        elapsed_time += 1
        time.sleep(2)
        transaction_receipt = fetchai_api.get_transaction_receipt(transaction_digest)
        if transaction_receipt is None:
            continue
        is_settled = fetchai_api.is_transaction_settled(transaction_receipt)
        not_settled = not is_settled
    assert transaction_receipt is not None, "Failed to retrieve transaction receipt."
    assert is_settled, "Failed to verify tx!"
    tx = fetchai_api.get_transaction(transaction_digest)
    is_valid = fetchai_api.is_transaction_valid(
        tx, fc2.address, account.address, "", amount
    )
    assert is_valid, "Failed to settle tx correctly!"
    assert tx == transaction_receipt, "Should be same!"
```

## Converting Agents to be ready for Mainnet v2

* Ask David M to fill this in and link to correct place in the AEA docs. 

## Ledger support and APIs

There is an API for you to find out from the block explorer a list of transactions associated with a given address. Here is an example:

https://explore-agent-land.fetch.ai/api/transactions?address=fetch193vvag846gz3pt3q0mdjuxn0s5jrt39fsjrays&offset=0&limit=100

This will fetch the last 100 transactions associated with the named address in JSON format.

### Hardware Wallets

All of the Fetch incentivised testnets support hardware wallets, such as the Ledger Nano S and X. More information on this will be published throughout Q4 including blog post tutorials on how to manage the process. 

## Roadmap for Smart Contracts

Mainnet V2 and the current testnet do not support the same smart contract language as mainnet version 1. When mainnet V2 is released, smart contracts will be developed using Cosmwasm, which will include the ability to develop your contracts in a number of languages depending on your preferences, such as Rust, Go or Javascript. You can get an introduction to this here.

Early incentivised testnet phases will use the EVM to be ethereum compatible, but later ones will fully embrace Cosmwasm and its powerful approach to building smart contracts. For more information on Cosmwasm, and Rust, the primary language in which contract development is currently done, you can go to https://www.cosmwasm.com/ and https://github.com/CosmWasm/cosmwasm-template

[version 0.2, TWS, 19th October 2020]





