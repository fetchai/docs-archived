Fetch.ai charges developers for computation and storage of data on the Fetch.ai Ledger in a manner which incentivises good coding practices.

With the best use of Fetch.ai Ledger types such as `State` and `ShardedState`, you can limit the fees by distributing data storage over a minimum number of shards.

Fees rise in a linear manner per number of shards up to the maximum number of shards.

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>The following information details the current implementation which is likely to change.<p>
</div>

## Calculating charge units

-   Storing data on the Fetch network costs 2 units per byte.

-   Performing computation on the Fetch network costs 1 unit per operation.

```bash
TOTAL_UNITS = ((2*storage) + computation) * number of shards
```

You can find out the total size of `etch` variables <a href="../.././etch-language/variables/#data-size" target=_blank>here</a>.

## Calculating total transaction fee

To calculate the transaction fee, multiply the total units by the charge rate given in FET or denominations thereof.

```bash
TOTAL_FEE = TOTAL_UNITS * CHARGE_RATE
```

The Fetch.ai Ledger uses the charge rate to prioritise the order of the incoming transactions in the same way as the Ethereum and Bitcoin networks do with gas and transaction fees respectively.

<br/>
