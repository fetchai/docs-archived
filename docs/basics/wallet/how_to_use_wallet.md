## Deposit Tokens

To transfer funds to your account on the Fetch wallet, you need to use its address as the destination account in the wallet or application you are using to send the funds. 

This address can be used to send supported tokens using the (native) fetch network.

### To copy your account's address

1. Either click on the account address at the top of the dashboard (below the account name):
![Copy active account address](../../images/wallet/address_copy.jpg)
2. Or select **Deposit** and scan the QR code.

Once you send the tokens, the balance should be updated.

!!! note
    If your origin wallet says that the address (which should start with "fetch") is invalid, it is probably expecting an ethereum address (beginning with "0x") and is most likely trying to send ERC20 FET. In this case, you need to use the [token bridge](https://token-bridge.fetch.ai/) to swap your ERC20 FET for native FET.

!!! warning
    You should **not** send ERC20 FET to this wallet. If you do, you will lose your tokens. The Fetch wallet can only hold native FET tokens and not ERC20 FET tokens.

## Send Tokens

To send tokens from your account:

Select **Send**.

Fill in the details of your transaction:

- **Recipient**: the address you want to send the tokens to.
- **Token**: the token denomination (the default should be ok).
- **Amount**: the number of tokens you want to send with this transaction (you can see how much funds you have above the Amount).
- **Memo** (Optional): some transactions (e.g. to/from some exchanges) require need to have a specific memo. If not needed, you can leave it blank.
- **Fee**: the transaction fee which you can choose from **Low**, **Average** and **High**.

!!! tip
    Usually, the lower the transaction fee, the longer you need to wait for your transaction to be settled on the network.

Press **Send**.

In the summary screen, review the details and if everything is correct, select **Approve**.

!!! tip
    You can check the status of your transaction via [the explorer](https://explore-fetchhub.fetch.ai).

## IBC transfer

_NOTE: In order to send IBC transactions, the "Show Advanced IBC Transfers" setting must be toggled on.
To navigate to the settings page from the dashboard, click on the hamburger menu (top-left).
Then click on "Settings"._

![Enable IBC tramsfer](../../images/wallet/enable_IBC_transfer.jpg)

Ensure that the desired origin network is selected on the dashboard (top-center).
If the origin network supports IBC, an "IBC Transfer" section will be visible towards the bottom of the dashboard.

![IBC tramsfer enabled](../../images/wallet/IBC_transfer_enabled.jpg)

Click the "Transfer" button in the "IBC Transfer" section.

Enter your mainnet destination chain address in the Recipient field, a MEMO (Optional), and click on Next to proceed.

![IBC tramsfer details](../../images/wallet/IBC_transfer_details.jpg)

Now enter the number of token you’d like to send to destination chain on the Amount field, select the preferred transaction fee then click Submit.
I suggest using Average or High fees at this time.

![IBC tramsfer amount details](../../images/wallet/IBC_transfer_amount.jpg)

On the transaction confirmation page, you can review the details of your transaction. Click on [Approve] to confirm.

![IBC tramsfer approve](../../images/wallet/IBC_transfer_approve.jpg)

### ⚛️ Congratulations & Welcome to the IBC Gang! ⚛️

✏ Notes:

- All IBC Hubs have their own channel ID and knowing this channel ID is necessary to perform the IBC transaction.

- Don’t send tokens via [Interchain Transfer] directly to a CEX: this can cause in most cases the loss of the funds.

## First-time origin/destination transfer

Before transferring between any given origin and destination combination for the first time, IBC channels must be configured in the wallet.

Click the "Select Chain" drop-down.
Click "+ New IBC Transfer Channel".

![Add IBC channel](../../images/wallet/add_IBC_channel.jpg)

Select the **destination** chain and enter the **source** channel ID (e.g. "channel-100").
Click "Save".

✏ Notes:

- If you write the wrong number on the Destination Chain Channel ID, extension will reject the operation with the warning "Failed to fetch the channel".

- Remember that you must write the channel ID in lower case (i.e. channel-X)
