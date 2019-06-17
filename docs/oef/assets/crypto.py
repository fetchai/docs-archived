# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
import base58
import logging

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, utils

logger = logging.getLogger(__name__)


class CryptoError(Exception):
    """Exception to be thrown when cryptographic signatures don't match!."""


CHOSEN_ALGORITHM_ID = b'MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAE'
CHOSEN_PBK_LENGTH = 160


class Crypto(object):
    def __init__(self):
        """
        Instantiate a crypto object.
        """
        self._chosen_ec = ec.SECP384R1()
        self._chosen_hash = hashes.SHA256()
        self._private_key = self._generate_pk()
        self._public_key_obj = self._compute_pbk()
        self._public_key_pem = self._pbk_obj_to_pem(self._public_key_obj)
        self._public_key_b64 = self._pbk_pem_to_b64(self._public_key_pem)
        self._public_key_b58 = self._pbk_b64_to_b58(self._public_key_b64)
        self._fingerprint_hex = self._pbk_b64_to_hex(self._public_key_b64)
        assert self._pbk_obj_to_b58(self._public_key_obj) == self._pbk_obj_to_b58(self._pbk_b58_to_obj(self._public_key_b58))

    @property
    def public_key(self) -> str:
        """
        Returns a 219 character public key in base58 format
        """
        return self._public_key_b58

    @property
    def public_key_pem(self) -> bytes:
        """
        Returns a PEM encoded public key in base64 format. It consists of an algorithm identifier and the public key as a bit string.
        """
        return self._public_key_pem

    @property
    def fingerprint(self) -> str:
        """
        Returns a 64 character fingerprint of the public key in hexadecimal format (32 bytes).
        :return: the fingerprint
        """
        return self._fingerprint_hex

    def _generate_pk(self) -> object:
        """
        Generates a private key.
        :return: private key
        """
        private_key = ec.generate_private_key(self._chosen_ec, default_backend())
        return private_key

    def _compute_pbk(self) -> object:
        """
        Derives the public key from the private key.
        :return: public key
        """
        public_key = self._private_key.public_key()
        return public_key

    def _pbk_obj_to_pem(self, pbk: object) -> bytes:
        """
        Serializes the public key from object to bytes.
        :param pbk: the public key as an object
        :return: the public key as a bytes string in pem format (base64)
        """
        result = pbk.public_bytes(encoding=serialization.Encoding.PEM, format=serialization.PublicFormat.SubjectPublicKeyInfo)
        return result

    def _pbk_pem_to_b64(self, pbk: bytes) -> bytes:
        """
        Converts the public key from pem bytes string format to standard bytes string format.
        :param pbk: the public key as a bytes string (PEM base64)
        :return: the public key as a bytes string (base64)
        """
        result = b''.join(pbk.splitlines()[1:-1])
        return result

    def _pbk_b64_to_b58(self, pbk: bytes) -> str:
        """
        Converts the public key from base64 to base58 string.
        :param pbk: the public key as a bytes string (base64)
        :return: the public key as a string (base58)
        """
        result = base58.b58encode(pbk).decode('utf-8')
        return result

    def _pbk_obj_to_b58(self, pbk: object) -> str:
        """
        Converts the public key from object to string.
        :param pbk: the public key as an object
        :return: the public key as a string (base58)
        """
        pbk = self._pbk_obj_to_pem(pbk)
        pbk = self._pbk_pem_to_b64(pbk)
        pbk = self._pbk_b64_to_b58(pbk)
        return pbk

    def _pbk_b58_to_b64(self, pbk: str) -> bytes:
        """
        Converts the public key from base58 string to base64 bytes string.
        :param pbk: the public key in base58
        :return: the public key in base64
        """
        pbk_b64 = base58.b58decode(str.encode(pbk))
        return pbk_b64

    def _pbk_b64_to_pem(self, pbk: bytes) -> bytes:
        """
        Converts the public key from standard bytes string format to pem bytes string format.
        :param pbk: the public key as a bytes string (base64)
        :return: the public key as a bytes string (PEM base64)
        """
        assert len(pbk) == CHOSEN_PBK_LENGTH, "Public key is not of expected length."
        assert pbk[0:32] == CHOSEN_ALGORITHM_ID, "Public key has not expected algorithm id."
        pbk = pbk[0:64] + b'\n' + pbk[64:128] + b'\n' + pbk[128:] + b'\n'
        pbk_pem = b'-----BEGIN PUBLIC KEY-----\n' + pbk + b'-----END PUBLIC KEY-----\n'
        return pbk_pem

    def _pbk_b58_to_obj(self, pbk: str) -> object:
        """
        Converts the public key from string (base58) to object.
        :param pbk: the public key as a string (base58)
        :return: the public key object
        """
        pbk = self._pbk_b58_to_b64(pbk)
        pbk = self._pbk_b64_to_pem(pbk)
        pbk_obj = serialization.load_pem_public_key(pbk, backend=default_backend())
        return pbk_obj

    def sign_data(self, data: bytes) -> bytes:
        """
        Sign data with your own private key.
        :param data: the data to sign
        :return: the signature
        """
        digest = self._hash_data(data)
        signature = self._private_key.sign(digest, ec.ECDSA(utils.Prehashed(self._chosen_hash)))
        return signature

    def is_confirmed_integrity(self, data: bytes, signature: bytes, signer_pbk: str) -> bool:
        """
        Confirrms the integrity of the data with respect to its signature.
        :param data: the data to be confirmed
        :param signature: the signature associated with the data
        :param signer_pbk:  the public key of the signer
        :return: bool indicating whether the integrity is confirmed or not
        """
        signer_pbk = self._pbk_b58_to_obj(signer_pbk)
        digest = self._hash_data(data)
        try:
            signer_pbk.verify(signature, digest, ec.ECDSA(utils.Prehashed(self._chosen_hash)))
            return True
        except CryptoError as e:
            logger.exception(str(e))
            return False

    def _hash_data(self, data: bytes) -> bytes:
        """
        Hashes data.
        :param data: the data to be hashed
        :return: digest of the data
        """
        hasher = hashes.Hash(self._chosen_hash, default_backend())
        hasher.update(data)
        digest = hasher.finalize()
        return digest

    def _pbk_b64_to_hex(self, pbk: bytes) -> str:
        """
        Hashes the public key to obtain a fingerprint.
        :return: the fingerprint in hex format
        """
        pbk_hash = self._hash_data(pbk)
        pbk_hex = pbk_hash.hex()
        return pbk_hex