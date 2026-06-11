
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from argon2.low_level import hash_secret_raw, Type

SALT_SIZE = 16
NONCE_SIZE = 12
KEY_SIZE = 32  # 256-bit

def derive_key(password: str, salt: bytes) -> bytes:
    return hash_secret_raw(
        secret=password.encode(),
        salt=salt,
        time_cost=3,
        memory_cost=64 * 1024,
        parallelism=2,
        hash_len=KEY_SIZE,
        type=Type.ID
    )

def encrypt(data: bytes, password: str) -> bytes:
    salt = os.urandom(SALT_SIZE)
    key = derive_key(password, salt)

    nonce = os.urandom(NONCE_SIZE)
    aesgcm = AESGCM(key)

    ciphertext = aesgcm.encrypt(nonce, data, None)

    # format: [salt][nonce][ciphertext]
    return salt + nonce + ciphertext

def decrypt(blob: bytes, password: str) -> bytes:
    salt = blob[:SALT_SIZE]
    nonce = blob[SALT_SIZE:SALT_SIZE + NONCE_SIZE]
    ciphertext = blob[SALT_SIZE + NONCE_SIZE:]

    key = derive_key(password, salt)

    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ciphertext, None)
