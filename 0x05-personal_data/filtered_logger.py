#!/usr/bin/env python3
import re
import typing
List = typing.List


def filter_datum(fields: List[str], redaction_str: str, message: str,
                 separator: str) -> str:
    """ filter_datum function """
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                              f'{field}={redaction_str}{separator}', message)
    return message
