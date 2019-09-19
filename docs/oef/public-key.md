A valid public key in the OEF contains only Base58 characters, which consist of alphanumeric characters, excluding the following characters: `0` (zero), `O` (capital o), `I` (capital i)
and `l` (lower case L).

You can generate test addresses with the  the <a href="https://github.com/fetchai/ledger-api-py" target=_blank>`ledger-api-py`(Python SDK)</a>. Check the documentation <a href="../../smart-contracts/executing-smart-contract-code/#public-keys" target=_blank>here</a>.

Or...

Generate a public key for your Agent with the <a href="/oef/assets/crypto.py" download="">`crypto.py`</a> script which uses the Python `cryptography` library.

Simply instantiate a `Crypto` object and call the `public_key()` function. 

``` python
@property
def public_key(self) -> str:
    """
    Returns a 219 character public key in base58 format
    """
    return self._public_key_b58
```

The library generates a private key and the function returns a Base58 public key string. 

Calling `public_key()` again returns the same public key.

In the same script, there are data verification and signing functions. 

The `sign_data()` function takes a serialized byte stream of data, signs it, and returns signed data as an immutable sequence of bytes.

``` python
def sign_data(self, data: bytes) -> bytes:
	"""
    Sign data with your own private key.
    :param data: the data to sign
    :return: the signature
    """
    digest = self._hash_data(data)
    signature = self._private_key.sign(digest, ec.ECDSA(utils.Prehashed(self._chosen_hash)))
    return signature
```

The `is_confirmed_integrity()` function verifies signed data against a signature and a public key.

``` python
def is_confirmed_integrity(self, data: bytes, signature: bytes, signer_pbk: str) -> bool:
   	"""
    Confirrms the integrity of the data with respect to its signature.
    :param data: the data to be confirmed
    :param signature: the signature associated with the data
    :param signer_pbk:  the public key of the signer
    :return: bool indicating whether the integrity is confirmed or not
    """
    signer_pbk = self._pbk_to_obj(signer_pbk)
    digest = self._hash_data(data)
    try:
    	signer_pbk.verify(signature, digest, ec.ECDSA(utils.Prehashed(self._chosen_hash)))
       	return True
   	except CryptoError as e:
       	logger.exception(str(e))
        return False
```



<br/>

