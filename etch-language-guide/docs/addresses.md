<h1>Address</h1> 

An `Address` is a data structure that represents a cryptographic public key, i.e. `OWNER_PUB_KEY`.

It is an uncompressed canonical <a href="https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm" target="_blank">ECDSA</a> 64 byte binary array which is `Base64` encoded.

!!! note
	The structure of an `Address` type may change to `Base58` in the future.

Instantiate an `Address` with an 88 character length string like this:

``` java
function main()

	var account = Address("AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8gISIjJCUmJygpKissLS4vMDEyMzQ1Njc4OTo7PD0+Pw==");

endfunction
```

!!! note
	When you use a `State` to represent an `Address` owner along with balance, supply a default value of `0` for the balance. If there is no current record on the ledger, it is considered a new `Address` and the default value is valid. 


## Verification

The `Address` type has a function `signed_tx()` which allows you to verify the signature. It returns a boolean.

``` java
function main()

	var account = Address("AAECAwQFBgcICQoLDA0ODxAREhMUFRYXGBkaGxwdHh8gISIjJCUmJygpKissLS4vMDEyMzQ1Njc4OTo7PD0+Pw==");
	var verified : Bool;
	verified = account.signed_tx();
	printLn(toString(verified));

endfunction
```

