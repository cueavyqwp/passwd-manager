import argon2
import base64


def derive_passwd(passwd: str) -> str:
    salt = passwd.encode().ljust(16, b"@")[-16:]
    key = argon2.low_level.hash_secret_raw(
        passwd.encode(), salt, 3, 65536, 2, 64, argon2.low_level.Type.I)
    return base64.urlsafe_b64encode(key).decode("utf-8")
