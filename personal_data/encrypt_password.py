#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""_encrypt_password.py_
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hache un mot de passe avec un sel en utilisant bcrypt.

    :param password: Le mot de passe à hacher.
    :type password: str
    :return: Le mot de passe haché.
    :rtype: bytes
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)

    return hashed
