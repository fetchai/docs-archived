# Creating Fetch.ai Native Wallets using `pocketbook`

`pocketbook` is a Python command line utility that provides a simple wallet mechanism for Fetch.ai’s main network. It allows you to create accounts, manage them, view token balances and transfer native FET from one address to another. `pocketbook` works with all of Fetch.ai’s native networks, including any test networks as well as the main network itself. It is simple to use, simple to install and is the easiest way of creating wallets to hold native FET for utility purposes on the networks, such as for performing transactions, or deploying and using synergetic and/or ai-powered smart contracts.

**Firstly, a warning:**

>**You use this application at your own risk**. Whilst Fetch.ai have made every
effort to ensure its reliability and security, it comes with no warranty. It is
intended for the creation and management of Fetch.ai mainnet wallets and
transactions between them. You are responsible for the security of your own
private keys (see `~/.pocketbook` folder). Do not use this application for
high-value operations: it is intended for utility operations on the main network.

That out of the way, let us proceed. You can view the source code for `pocketbook` on Fetch.ai’s [GitHub account](https://github.com/fetchai/tools-pocketbook). You can download, view, modify and use the source code directly, or you can get it via PyPI:

```
pip3 install -U pocketbook
```

Note the `-U` option that will update your existing installation if it is already installed.

`pocketbook` defaults to access the main network. You can change the network using the `-n` parameter. E.g.:

```
pocketbook -n testnet …
pocketbook -n mainnet …
```

For details of how to use `pocketbook`, you can use its help option `-h`. You can get help on all the commands by appending `-h`. The remainder of this document covers the four key operations that you will need in the majority of cases:

Creating a new address
Adding an existing address
Listing addresses and balances
Transferring tokens from one address to another
Backing up your private keys

### Creating a new address

To create a new address simply run the following command:

```
pocketbook create
```

You will be prompted to enter a name for this key pair, followed by a password for the key. Below is a sample output:

```
Enter name for key: foo
Enter password for key...:
Confirm password for key.:
```

### Adding an existing address

Other users may provide you with an address, and you can add it to `pocketbook`’s address book. Once you have added it, you can send tokens to it, or query the balance. You can add existing addresses like this:

```
pocketbook -n mainnet add <name-for-the-address> <address>
```

### Listing addresses and balances

You can query the balance of your accounts and address book entries with the following command:

```
pocketbook -n mainnet list [-v]
```

Adding the `-v` option will display the addresses alongside the names and balances.

### Making a transfer

You can use `pocketbook`’s `transfer` command to send tokens from one address to another. The syntax is as follows:

```
pocketbook -n mainnet transfer <destination-name> <amount> <signer (source)>
```

If you wish to transfer 10 FET from account `main` to account `other`, you would use the transfer command like this:

```
pocketbook -n mainnet transfer other 10 main
```

You will then be prompted with a summary of the transfer so that you can verify the details before you agree to the transfer. You can type `CTRL-C` to abort at any time. This confirmation will look like this:

```
Network....: devnet
From.......: main
Signers....: ['main']
Destination: dest_address_will_be_here
Amount.....: 10 FET
    
Press enter to continue
```

If you are happy with the transfer, press enter, enter the password for the source account (in this case, `main`) and the transaction will be submitted. 

### Backing up your accounts and address book

`pocketbook` stores all information in the `~/.pocketbook` folder on your computer. You can back this folder up entirely to store your encrypted private keys. We **strongly recommend** that you do this regularly and keep the backups in an encrypted safe place in order to provide a mechanism for recovering your accounts.


