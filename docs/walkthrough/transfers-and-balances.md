# Making transfers

In order to make transfers in the network, you first need to create an address. Please see the [tutorial](/walkthrough/creating-addresses) describing several available ways to do so. We'll be using the address we minted in that tutorial, `2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5`. Note that if you use the same address, we might all be fighting over the same test tokens! :)

## Using Pocketbook
You can use Pocketbook to send tokens to someone who has provided you with their address, but obviously you won't know their private key. In order to do so, you need to use a command like the following:

``` bash
pocketbook -n <network> transfer <destination-name> <amount> <signer (source)>
```

For our particular example:

```
$ pocketbook -n testnet transfer GeneratedTestnetAddress 100 TestNetAddress
Network....: testnet
From.......: TestNetAddress
Signer(s)..: TestNetAddress
Destination: GeneratedTestnetAddress: 2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5
Amount.....: 100.0000000000 FET
Fee........: 0.0000000001 FET
Total......: 100.0000000001 FET (Amount + Fee)

Press enter to continue
Enter password for key TestNetAddress: 
Submitting TX...
Submitting TX...complete
```

And now, if we check the balance, we see:

```
$ pocketbook -n testnet ls -v
Name                    Type Balance          Stake Address
GeneratedTestnetAddress addr 100.0            0.0   2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5
```

## Using the Python Ledger API

Now let's do the same thing, but this time programmatically.

The minimum code to show the balance in an address is:

``` python
from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address

# Connect the API to the testnet endpoint
try:
	api = LedgerApi(network="testnet")
except Exception as e:
	sys.exit(e)

# Show balance
# Correct from the smallest FET unit to actual FET for nicer display
units_in_fet = 10000000000
print("Balance:", api.tokens.balance("2uGQSyM56XfkaFeoyYib2dt4rvFwVZ6if5JREZd54d1sNehEQ5") / 10000000000)
```

And the output when it is executed is:

```
$ python3 balance.py
Balance: 100.0
```

Voila, it is 100 FET, as expected after the transfer in the previous section (although it may not be when you get to that account!).

Now let's transfer 10 FET out of this account to another one that I have created. Here is the code required to do it:

```
from fetchai.ledger.api import LedgerApi, TokenApi
from fetchai.ledger.contract import Contract
from fetchai.ledger.crypto import Entity, Address

# Connect the API to the testnet endpoint
try:
	api = LedgerApi(network="testnet")
except Exception as e:
	sys.exit(e)

# Create our source address (WARNING: this is a shared private key used in
# the tutorial. You MUST NOT store keys in plain sight like this!)
entity = Entity(b'4\x1f\x00\xf7\x89\x00c\xee\xfd5h\xf2\xf5\xc7\xc3\x10\x80/\xd3+:\x15\xa1\x11\xac\x0f\xbf\xb4\xa6\\\xe0{')
address = Address(entity)

# Set target address
target_address = "2QaAtmWr7xcaqKfncWrtY6izkjk81nfGWkusoMNd1wri2FS7so"
amount = 10

# Show balances before the transfer
# Correct from the smallest FET unit to actual FET for nicer display
units_in_fet = 10000000000
print("Source balance before:", api.tokens.balance(address) / units_in_fet)
print("Target balance before:", api.tokens.balance(target_address) / units_in_fet)

# Trigger the transaction
try:
	api.sync(api.tokens.transfer(entity, target_address, amount * units_in_fet, 20))
except Exception as e:
	sys.exit(e)

# Show balances after the transfer
print("Source balance after:", api.tokens.balance(address) / units_in_fet)
print("Target balance after:", api.tokens.balance(target_address) / units_in_fet)
```

And this is the output of the program:

```
$ python3 simple_transfer.py
Source balance before: 100.0
Target balance before: 0.0
Source balance after: 89.9999999999
Target balance after: 10.0
```

!!! warning "**Do not expose private keys in source code**"
    For the sake of simplicity, in this code snippet we are exposing the private key in the source code, *which is very bad practice*. Better ways of handling this would be:

    - Pass in the key as a command line parameter
    - Pass in the encrypted key, ask for password, decrypt and use

