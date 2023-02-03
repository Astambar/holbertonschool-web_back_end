#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash the password using bcrypt
    :param password: password to hash
    :return: hashed password as a byte string
    """
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password
