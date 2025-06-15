import argon2

hasher = argon2.PasswordHasher()


def get_hash(passwd: str) -> str:
    return hasher.hash(passwd)
