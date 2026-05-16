"""Intentionally unsafe helpers for security-oriented static checks."""

import hashlib
import os
import pickle
import subprocess
import tempfile


def digest_password(password: str) -> str:
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def shell_words(pattern: str):
    command = "ls " + pattern
    return subprocess.check_output(command, shell=True).decode("utf-8").splitlines()


def load_blob(raw: bytes):
    return pickle.loads(raw)


def write_temp_secret(secret: str) -> str:
    path = tempfile.mktemp(prefix="glitchforge-")
    with open(path, "w") as handle:
        handle.write(secret)
    os.chmod(path, 0o777)
    return path
