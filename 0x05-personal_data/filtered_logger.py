#!/usr/bin/env python3
import re


def filter_datum(fields, redaction, message, separator):
    """
    Obfuscates sensitive fields in log messages
    """
    for field in fields:
        message = re.sub(r"{}=[^;]*".format(field), "{}={}".format(field, redaction), message)
    return message