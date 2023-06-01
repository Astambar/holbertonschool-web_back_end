#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""_filtered_logger.py_
"""

import re
import logging
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """
    Renvoie le message de journal avec les champs spécifiés obfusqués.

    :param fields: une liste de chaînes représentant
                      tous les champs à obfusquer

    :param redaction: une chaîne représentant par quoi le champ sera obfusqué

    :param message: une chaîne représentant la ligne de journal

    :param separator: une chaîne représentant par quel caractère tous les
                         champs sont séparés dans la ligne de journal (message)

    :return: une chaîne représentant le message de journal
                avec les champs spécifiés obfusqués
    """
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """_init_

        Args:
            fields (List[str]): _description_
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """_format_

        Args:
            record (logging.LogRecord): _description_

        Returns:
            str: _description_
        """
        return filter_datum(self.fields,
                            self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)
