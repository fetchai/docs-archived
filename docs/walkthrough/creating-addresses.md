# *Part 1: Creating addresses and getting testnet tokens*

Welcome to part 1 of the step-by-step tutorial introducing you to Fetch.ai. Over several parts, we'll go from creating addresses through transactions to deploying and interacting with smart contracts. Later we'll also look at node deployment, and the creation of autonomous economic agents. In this first part, though, we will focus on how you can get testnet addresses and stock them with tokens. With the exception of the free-tokens bit, everything here also applies to mainnet.

First things first, it's the perfect time to install `pocketbook`, our command-line based Python wallet and address book. It's easy to install in Linux and on the Mac. Open a Terminal window and type:

```
pip3 install -U pocketbook
```

The `-U` option is important as it ensures that if you already have it installed, it will upgrade where applicable.

This will also install the Python Ledger API [https://github.com/fetchai/ledger-api-py](https://github.com/fetchai/ledger-api-py), which gets you up and running with your own code. You can find on-line docs for using `pocketbook` on our [https://docs.fetch.ai](https://docs.fetch.ai) site at [https://docs.fetch.ai/getting-started/wallet/](https://docs.fetch.ai/getting-started/wallet/).

## How to create wallets

Let's get started with a simple program that generates an address and outputs the public address and private key. Quite obviously, any private key you generate should be kept secure, etc., but you will occasionally need this in order to deploy and interact with contracts. So here's a little Python code that does this:
```
# No warranty, your own risk, etc. Provided for reference and example!

from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address

print ("Fetch.ai Address Generator v1.0")

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
Neat, eh?

When you run this, it will output the private key (hex and in bytes) and the address (which you can add to `pocketbook` or use to receive tokens from others).

For example, if you save the above file into a program called `generate_address.py`, you can run it and will get a result like this:
```
$ python3 generate_address.py 
Fetch.ai Address Generator v1.0
Private key:  341f00f7890063eefd3568f2f5c7c310802fd32b3a15a111ac0fbfb4a65ce07b
           :  b'4\x1f\x00\xf7\x89\x00c\xee\xfd5h\xf2\xf5\xc7\xc3\x10\x80/\xd3+:\x15\xa1\x11\xac\x0f\xbf\xb4\xa6\\\xe0{'
    Address:  2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5
```
Needless to say, don't use that account for anything, it's shared with you all, private key and all. But you get the idea. Just to reiterate, *any account you wish to use yourself, do not, ever, for any reason, disclose the private key in public, on the internet, or anywhere people can see it* so don't post the output of the above program here!

If we now wanted to add this address to `pocketbook`'s address book, we could do it with this, incidentally (but do see the docs linked above):
```
pocketbook -n testnet add GeneratedTestnetAddress 2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5
```
It would be *our* responsibility to store the private key to this securely.

So that shows a bunch of things:

1. Getting pocketbook installed, and the Python API along with it
2. Writing a simple Python program to generate an address
3. Adding that address into pocketbook's address book

Addresses generated inside pocketbook will have the private keys encrypted and secured, so you don't need to store them manually (but you do need to back them up yourself — instructions are here: https://docs.fetch.ai/getting-started/wallet/)

For testnet addresses only, you can also use our web-based wallet, which is at https://testnet-wallet.fetch.ai/

## How to get testnet tokens

When you have an address, you'll need some tokens.

There are three easy ways of getting tokens on testnet:

1. *Use our new token tap!* Go here — https://explore-testnet.fetch.ai/tokentap — paste the Address in and press the DISPENSE button. Wait 30-60 seconds and voila, you'll have 10-500 test-FET just like that. Using our above example, you can send the above “free for all” account tokens by pasting `2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5` into the address box.
2. *Transfer tokens from another account you have!* It's easy, you can use `pocketbook` and it takes no time at all. Just use the `pocketbook -n testnet transfer destination_account_name AMOUNT source_account_name` syntax and you're done.
3. *Ask in the [Fetch developer slack](https://join.slack.com/t/fetch-ai/shared_invite/enQtNDI2MDYwMjE3OTQwLWY0ZjAyYjM0NGQzNWRhNDMxMzdjYmVhYTE3NDNhNTAyMTE0YWRkY2VmOWRmMGQ3ODM1N2NjOWUwNDExM2U3YjY)*. We have tons, and we're happy to send large amounts if you need them for specific contracts or tests. *Don't be shy*, we want you to get stuff done. It may take a day or two, but we'll do our best to make it quick.

That's it for part 1, in which we've learned how to create addresses that work on testnet and mainnet, and how to get tokens for them.

In part 2, we'll be doing transactions in code and transactions using pocketbook to get you moving things around easily.

