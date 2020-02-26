# Transfers and balances

This is a relatively short piece that gets you going using `pocketbook` and the Python API to perform a transfer and check balances. So let’s do the easy one first, `pocketbook`. We’ll be using the address we minted in part 1, `2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5`. Obviously, you’re able to use that address too, as the private key is in part 1’s text, but it’s not recommended or we might all be fighting over the same test tokens!
```
$ pocketbook -n testnet add SharedTestNetProbablyDontUse 2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5
$ pocketbook -n testnet ls -v
Name                         Type Balance          Stake Address                                            
SharedTestNetProbablyDontUse addr 0.0              0.0   2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5 
$ 
```
This is a simple use of `pocketbook` as an address book. We add the public address. You can use this where you are strictly using the address book feature, e.g., a friend or someone you want to send tokens to has provided you with their address, but obviously you won’t know their private key. We’re going to use `pocketbook` to transfer some tokens in:
```
$ pocketbook -n testnet transfer SharedTestNetProbablyDontUse 100 TestNetAddress
Network....: testnet
From.......: TestNetAddress
Signer(s)..: TestNetAddress
Destination: SharedTestNetProbablyDontUse: 2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5
Amount.....: 100.0000000000 FET
Fee........: 0.0000000001 FET
Total......: 100.0000000001 FET (Amount + Fee)

Press enter to continue
Enter password for key TestNetAddress: 
Submitting TX...
Submitting TX...complete
$ 
```
And now, if we check the balance, we see:
```
SharedTestNetProbablyDontUse addr 100.0            0.0   2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5
```
So that shows some simple things: we’ve added an existing address (like one that we create using [part 1](../walkthrough/creating-addresses.md)'s Python code), we’ve transferred some tokens to it using `pocketbook` and we’ve checked its balance. Lovely.

Now let’s do the same thing, but this time in code, using the Python API! Balance first, here’s the code:
```
from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address

# this gets us an API connected to the testnet endpoint:
try:
	api = LedgerApi(network="testnet")
except Exception as e:
	sys.exit(e)
	
print("Balance:", api.tokens.balance("2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5") / 10000000000)
```
Easy, right?

Firstly, the same code you’ve seen before, to get hold of the Python API for use. Then one, simple, line that gets the balance of the address we’ve been using and shows it on the screen. Note that we’re dividing it by 10,000,000,000 -- this corrects from the _smallest FET unit_ to actual FET. Let’s run this code:
```
$ python3 balance.py
Balance: 100.0
$ 
```
Voila, it’s 100, as we expect (it may not be when you get to that account!)

Now let’s do a transfer, instead. I’m going to transfer 10 FET out of this account to another one that I have created. Here’s the result of the code:
```
$ python3 simple_transfer.py
Source balance before 100.0
Target balance before 0.0
Source balance after 89.9999999999
Target balance after 10.0
$ 
```
And here’s the code that did it:
```
from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address

# this gets us an API connected to the testnet endpoint:
try:
	api = LedgerApi(network="testnet")
except Exception as e:
	sys.exit(e)
	
# create our source address (WARNING: this is a SHARED private key used in the 
# tutorial. You would NEVER store keys in plain sight like this!)
# There are far better ways of handling this, e.g.:
# - Pass in the key as a command line parameter
# - Pass in the encrypted key, ask for password, decrypt and use
entity = Entity(b'4\x1f\x00\xf7\x89\x00c\xee\xfd5h\xf2\xf5\xc7\xc3\x10\x80/\xd3+:\x15\xa1\x11\xac\x0f\xbf\xb4\xa6\\\xe0{')
address = Address(entity)

# Set target address:
target_address = "2QaAtmWr7xcaqKfncWrtY6izkjk81nfGWkusoMNd1wri2FS7so"
amount = 10
	
# Show where we are before we start:
print("Source balance before", api.tokens.balance(address) / 10000000000)
print("Target balance before", api.tokens.balance(target_address) / 10000000000)

# Trigger the transaction:
try:
	api.sync(api.tokens.transfer(entity, target_address, amount * 10000000000, 20))
except Exception as e:
	sys.exit(e)

# Show where we are now we're done:
print("Source balance after", api.tokens.balance(address) / 10000000000)
print("Target balance after", api.tokens.balance(target_address) / 10000000000)
```
This is, of course *highly simplified*, and there are better ways of structuring it. For a start, all those `/ 10000000000`s are exhausting to look at, and furthermore, we’re exposing the private key again in the source code, *which is very bad practice*. In an upcoming part, we’ll look at how we tidy all this up and write better code. But next up is [part 3](../walkthrough/smart-contracts.md), where *we look at deploying and interacting with smart contracts!*

