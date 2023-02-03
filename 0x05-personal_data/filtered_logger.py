#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
import re
import typing
List = typing.List
sub = re.sub

def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ filter_datum function """
    for field in fields:
        message = sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message
