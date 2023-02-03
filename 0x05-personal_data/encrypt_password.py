#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def is_valid(hashed_password, password):
    password = password.encode('utf-8')
    return bcrypt.checkpw(password, hashed_password)
