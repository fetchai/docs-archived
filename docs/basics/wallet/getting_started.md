The Fetch Wallet allows you to interact with the Fetch network via your browser.

## Compatibility

The Fetch Wallet works on all Chromium-based web browsers, including [Chrome](https://www.google.com/chrome/), [Brave](https://brave.com), [Edge](https://www.microsoft.com/edge) and [Decentr](https://decentr.net).

## Get the Wallet

Install the Fetch wallet from the [Chrome web store](https://chrome.google.com/webstore/detail/fetchai-network-wallet/ellkdbaphhldpeajbepobaecooaoafpg/related?hl=en-GB).

!!! info
    At this time, you cannot run the [Keplr](https://chrome.google.com/webstore/detail/keplr/dmkamcknogkgcdfhhbddcghachkejeap?hl=en) and Fetch wallets together because they interfere. Please disable the Keplr wallet before using the Fetch wallet.

## Set up

After opening the wallet for the first time, you will see the option to:

- [Create a new account](#to-create-a-new-account)
- [Import an existing account](#import-an-existing-account)
- [Connect your ledger hardware wallet](#use-ledger-hardware-wallet)

### To Create a New Account

* Select `Create new account`
* Backup your mnemonic seed securely.

    !!! warning
        **KEEP IT SAFE!** Anyone with your mnemonic seed can access your wallet and take your assets.
    !!! danger
        **DON'T LOSE IT!** Lost mnemonic seed cannot be recovered! If you lose your mnemonic seed you will lose access to your wallet.

* Give your account a name and set a password. This password will be used the next time you want to use the wallet or make important changes to your account.
* Rearrange the mnemonic phrases by clicking on them in the correct order to confirm your mnemonic seed.

### To Import an Existing Account

If you have an account on the Fetch network, for example having had one already on the Fetch wallet and want to access it again, have an account on another wallet (e.g. Cosmostation, Keplr, ...) and wish to bring it to the Fetch wallet, or having created an address using one of our tools (e.g. the [AEA framework](https://docs.fetch.ai/aea)), you can import it into the Fetch wallet:

* Select `Import existing account`
* Enter your mnemonic seed (set of words) or private key (hexidecimal)

    !!! warning
        **KEEP IT SAFE!** Anyone with your mnemonic seed or private key can access your wallet and take your assets.

* Give your account a name and set a password. This password will be used the next time you want to use the wallet or make important changes to your account.

### To Use Ledger Hardware Wallet

If you have a [Ledger](https://www.ledger.com/) hardware wallet and wish to keep your key and mnemonics on that device while using the Fetch wallet:

!!! info
    Currently only [ledger](https://www.ledger.com/) hardware wallets are supported.

* Select `Import ledger`
* Give your account a name and set a password. This password will be used the next time you want to use the wallet or make important changes to your account.
* Follow the instructions on the popup to connect your device.

!!! warning
    Please ensure you keep your mnemonic seed somewhere safe where others cannot access it. If you lose it, your wallet will be inaccessible once you log out. The password for your account should also be kept safe but is not necessary for recovery if you have your mnemonic seed.

!!! info
    If you lose your password, you need to uninstall and re-install the Fetch wallet and select `Import existing account`. Then use the mnemonic seed for your account and choose a new password.
