The `Transaction` type provides access to data pertaining to a currently invoking transaction on a running smart contract.

To access the `Transaction` type you need a <a href="../context" target=_blank>`Context`</a>.


## `getContext()`

Call `getContext()` from within a permitted <a href="../context#specific-annotated-functions" target=_blank>specific annotated function</a>.

From here, use the `transaction()` function to return the `Transaction` data.

``` c++
var context = getContext();
var tx = context.transaction();
```

With the variable `tx`, you now have access to a number of transaction functions.


## `digest()`

The `digest()` function returns the hash of the transaction in `UInt256` form.

``` c++
var context = getContext();
var tx = context.transaction();
var tx_digest = tx.digest();
```


## `from()`

The `from()` function returns the `Address` of the transaction sender.

``` c++
var context = getContext();
var tx = context.transaction();
var tx_sender = tx.from();
```



## `transfers()`

`transfers()` returns an array of <a href="../balance-transfer/" target=_blank>`Transfer`</a> types.

``` c++
var context = getContext();
var tx = context.transaction();
var tx_transfer = tx.transfers();
```




## `getTotalTransferAmount()`

The `getTotalTransferAmount()` returns a value for the total transfer amount in `UInt64`.

``` c++
var context = getContext();
var tx = context.transaction();
var tx_total_amount = tx.getTotalTransferAmount();
```


## `validFrom()`

The `validFrom()` function returns the starting block index.

``` c++
var context = getContext();
var tx = context.transaction();
var tx_valid_from = tx.validFrom();
```


## `validUntil()`

The `validUntil()` function returns a future block index.

``` c++
var context = getContext();
var tx = context.transaction();
var tx_valid_until = tx.validUntil();
```



## `chargeRate()`

The `chargeRate()` function returns the charge rate in `UInt64`.

``` c++
var context = getContext();
var tx = context.transaction();
var tx_charge_rate = tx.chargeRate();
```




## `chargeLimit()`

The `chargeLimit()` function returns the limit to the transaction charge in `UInt64`.

``` c++
var context = getContext();
var tx = context.transaction();
var tx_charge_limit = tx.chargeLimit();
```



## `contractDigest()`

The `contractDigest()` function returns the hash of the contract string in `UInt256` form.

``` c++
var context = getContext();
var tx = context.transaction();
var tx_contract_digest = tx.contractDigest();
```



## `contractAddress()`

The `contractAddress()` function returns the unique contract `Address`.

``` c++
var context = getContext();
var tx = context.transaction();
var tx_contract_address = tx.contractAddress();
```




## `action()`

The `action()` function returns the name of the currently invoking `@action` function.

``` c++
var context = getContext();
var tx = context.transaction();
var tx_action = tx.action();
```



## `signatories()`

The `signatories()` function returns an array of `Address` types.

``` c++
var context = getContext();
var tx = context.transaction();
var tx_signatories = tx.signatories();
```




## Example

!!!	Note
	Coming soon.



<br />
