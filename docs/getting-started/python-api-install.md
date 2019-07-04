Download and install the Python library which interacts with a running ledger node.

``` bash
git clone git@github.com:fetchai/ledger-api-py.git -b release/v0.5.x
```

!!!	Tip
	Make sure you are on the latest release branch in order to have the latest features. 

Install the library with the following command:

``` python
cd ledger-api-py/
python3 setup.py install
```

Find out how to build a smart contract using the Python API [here](../smart-contracts/submitting_contract.md).

<!--### Connecting to testnet

Navigate to the constellation application folder:

``` bash
cd apps/constellation
```

If you have been running a local network, delete the database files:

``` bash
rm -f *.db
```

Start the network connecting to the alpha test network.

``` bash
./constellation -bootstrap -network 
./constellation -bootstrap -network delta
```
-->



<br/>
