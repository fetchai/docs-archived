<h1>Address</h1> 

An `Address` is a data structure that represents a cryptographic public key, i.e. `OWNER_PUB_KEY`.

It is an uncompressed canonical <a href="https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm" target="_blank">ECDSA</a> 64 byte binary array which is hashed, then halfed, then a checksum of 4 bytes is added from the end of the original 64 bytes to make a 36 byte binary array which is then `Base58` encoded.

You can get an address string in the `python-ledger-api`.

And then in `etch`, you can instantiate an `Address` like this:

``` java
function main()

  var account = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");

endfunction
```

!!! note
	When you use a `State` to represent an `Address` owner along with balance, make sure you supply a default value of `0` for the balance. If there is no current record on the ledger, it is considered a new `Address`. 


## Verification

The `Address` type has a function `signed_tx()` which allows you to verify the signature. It returns a boolean.

``` java
function main()

  var account = Address("2ifr5dSFRAnXexBMC3HYEVp3JHSuz7KBPXWDRBV4xdFrqGy6R9");
  var verified : Bool;
  verified = account.signed_tx(); 
  printLn(toString(verified)); // False

endfunction
```

