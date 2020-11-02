## Building

```
    npm install && npm run build
``` 

## Adding built Extension to Chrome 

- update version in two places 1) manifest 2) package.json. When running if they are not then error in console should show when using extension
- build as above and then zip resultant prod folder which is the package to use in Chrome


## Changing  pre-existing currencies

- Add currency to NativeChainInfos file

### Run Cosmos locally

- Run a local instance of GAIA, with an account with a currency called "stake" specified in the genesis file.
- This can be achieved by following the installation instructions [here](https://hub.cosmos.network/master/gaia-tutorials/installation.html), and then these instructions for [starting](https://hub.cosmos.network/master/gaia-tutorials/deploy-testnet.html) a node. 
- Ensure the Cosmos RPC is started on the correct port by modifying the final command as follows

```
    gaiad start --rpc.laddr tcp://0.0.0.0:26657 
```

- If it is started on a different port change port ("26657") number in src/chain-info.ts to the desired port
- Navigate to chrome://extensions in chrome broswer select "developer mode"; select "Load unpacked"; choose /dist 
- After creating an account use gaiacli to add funds to that address 

```
    gaiacli tx send validator <your address>  10000000stake --chain-id testing
```

where `<your address>` is copied from the browser extension. 

### Changing this currency in chain-info (optional)

- To change currency name replace all instances of string "stake" in src/chain-info.ts file from to named currency eg fet
- In src/ui/components/form/coin-input.tsx Change string  "FET" (matchcase) in line containing string : 

```<span className={styleCoinInput.fet}>FET</span>``` 

to your chosen currency name eg stake
- Available balance current price refers to value of fet from coingecko. 
- To change the currency change the "coinGeckoId" variable in src/chain-info.ts to the coin gecko id of the desired currency. 
- After making changes rebuild with the following command

```
npm run dev
```

### Running in Firefox

build as above then navigate in Firefox to "about:debugging#/setup" then click "this firefox" then click "load temporary addon" then select 
.manifest file in dist directory.  It should fully work in Firefox. 

### Running Hardware wallet 

- I have limited it during development to require cosmos app version 2> which can be installed as follows. 
- change of configs (in config.ts) can be done to change required version (change variable "REQUIRED_COSMOS_APP_VERSION"),
- which is ok with >= 1.5 

### Steps to install the version:

- open Ledger Live
- connect your Ledger
- go to settings (top right icon)
- go to "Experimental features"
- activate "Manage Providers" and set it to number 4
- go to "Manager" to install apps
- look for the Cosmos App
- You should now see the version 2.2.2
- install that version on your Ledger Nano S or X
