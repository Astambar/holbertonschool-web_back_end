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

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Vérifie si un mot de passe correspond à un mot de passe haché.

    :param hashed_password: Le mot de passe haché.
    :type hashed_password: bytes
    :param password: Le mot de passe à vérifier.
    :type password: str
    :return: True si le mot de passe correspond au mot de passe haché, False sinon.
    :rtype: bool
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
