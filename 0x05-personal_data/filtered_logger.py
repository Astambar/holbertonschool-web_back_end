#!/usr/bin/env python3
import re
import typing
List = typing.List
substitute = re.sub


def filter_datum(fields: List[str], redaction_str: str, message: str,
                 separator: str) -> str:
    """ filter_datum function """
    for field in fields:
        message = substitute(f'{field}=(.*?){separator}',
                              f'{field}={redaction_str}{separator}', message)
    return message
