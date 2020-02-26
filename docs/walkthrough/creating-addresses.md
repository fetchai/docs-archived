# Creating addresses and getting testnet tokens

Welcome to part 1 of the step-by-step tutorial introducing you to Fetch.ai, where we will focus on how you can get testnet addresses and stock them with tokens. With the exception of the free-tokens bit, everything here also applies to mainnet.

First things first, it's the perfect time to install `pocketbook`, our command-line based Python wallet and address book.

!!! warning "**You use this application at your own risk**"
    Whilst Fetch.ai have made every effort to ensure its reliability and security, it comes with no warranty. It is intended for the creation and management of Fetch.ai mainnet wallets and transactions between them. You are responsible for the security of your own private keys (see `~/.pocketbook` folder). Do not use this application for high-value operations: it is intended for utility operations on the main network.

`pocketbook` can be easily installed in Linux and on the Mac. Open a terminal window and type:

``` bash
pip3 install -U pocketbook
```

The `-U` option ensures that if you already have it installed, it will upgrade where applicable.

`pocketbook` defaults to access the main network. You can change the network using the `-n` parameter. E.g.:

``` bash
pocketbook -n testnet <command>
pocketbook -n mainnet <command>
```

For details of how to use `pocketbook`, you can use its help option `-h`.


## Creating a new address

### Using Pocketbook

Simply run the following command:

``` bash
pocketbook create
```

You will be prompted to enter a name for this key pair, followed by a password for the key. Below is a sample output:

```
Enter name for key: foo
Enter password for key...:
Confirm password for key.:
```

### Using the web test net wallet

For testnet addresses only, you can also use our [web-based wallet](https://testnet-wallet.fetch.ai/). You will be prompted to enter the password for the address twice.

### Using the Python Ledger API

Installing `pocketbook` also installs the Python Ledger API ([GitHub repository](https://github.com/fetchai/ledger-api-py)), which enables you to create and interact with addresses programmatically.

Let's get started with a simple Python program that generates an address and outputs the private key (hex and in bytes) and the address; you can add the latter to `pocketbook` or use to receive tokens from others.

``` python
from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address

print ("My Fetch.ai Address Generator v1.0")

# this gets us an API connected to the testnet endpoint:
try:
	api = LedgerApi(network="testnet")
except Exception as e:
	sys.exit(e)
	
entity = Entity()
print ("Private key: ", entity.private_key_hex)
print ("           : ", entity.private_key_bytes)
print ("    Address: ", Address(entity))
```

For example, if you save the above file into a program called `generate_address.py`, you can run it and will get a result like this:
```
$ python3 generate_address.py 
Fetch.ai Address Generator v1.0
Private key:  341f00f7890063eefd3568f2f5c7c310802fd32b3a15a111ac0fbfb4a65ce07b
           :  b'4\x1f\x00\xf7\x89\x00c\xee\xfd5h\xf2\xf5\xc7\xc3\x10\x80/\xd3+:\x15\xa1\x11\xac\x0f\xbf\xb4\xa6\\\xe0{'
    Address:  2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5
```

!!! warning "**Do not use this account**"
    This account and its private key are shared with anyone who reads this tutorial. Just to reiterate, *any account you wish to use yourself, do not, ever, for any reason, disclose the private key in public, on the internet, or anywhere people can see it*. So don't post the output of the above program here!


## Adding an address to Pocketbook

We may now want to add the address we just created (or another provided by other users) to `pocketbook`. Once an address is added, you can send tokens to it or query the balance. You can add existing addresses like this:

``` bash
pocketbook -n <network> add <name-for-the-address> <address>
```

For our particular example:

``` bash
pocketbook -n testnet add GeneratedTestnetAddress 2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5
```

It would be *our* responsibility to store the private key to this securely. Addresses generated inside `pocketbook` will have the private keys encrypted and secured, so you don't need to store them manually (but you do need to back them up yourself).

## How to get testnet tokens

When you have an address, you'll need some tokens.

There are three easy ways of getting tokens on testnet:

1. *Use our new token tap!* Go here — https://explore-testnet.fetch.ai/tokentap — paste the Address in and press the DISPENSE button. Wait 30-60 seconds and voila, you'll have 10-500 test-FET just like that. Using our above example, you can send the above “free for all” account tokens by pasting `2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5` into the address box.
2. *Transfer tokens from another account you have!* It's easy, you can use `pocketbook` and it takes no time at all. Just use the `pocketbook -n testnet transfer destination_account_name AMOUNT source_account_name` syntax and you're done.
3. *Ask in the [Fetch developer slack](https://join.slack.com/t/fetch-ai/shared_invite/enQtNDI2MDYwMjE3OTQwLWY0ZjAyYjM0NGQzNWRhNDMxMzdjYmVhYTE3NDNhNTAyMTE0YWRkY2VmOWRmMGQ3ODM1N2NjOWUwNDExM2U3YjY)*. We have tons, and we're happy to send large amounts if you need them for specific contracts or tests. *Don't be shy*, we want you to get stuff done. It may take a day or two, but we'll do our best to make it quick.

That's it for part 1, in which we've learned how to create addresses that work on testnet and mainnet, and how to get tokens for them.

In part 2, we'll be doing transactions in code and transactions using pocketbook to get you moving things around easily.

