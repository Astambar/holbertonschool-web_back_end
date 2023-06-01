#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""_filtered_logger.py_
"""

import re
import os
import logging
import mysql.connector
from typing import List

connection = mysql.connector.connection

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Renvoie le message de journal avec les champs spécifiés obfusqués."""
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialise RedactingFormatter"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formate l'enregistrement de journal"""
        return filter_datum(self.fields,
                            self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Crée un objet logger"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> connection.MySQLConnection:
    """Renvoie un connecteur à la base de données"""
    username = os.environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    db_name = os.environ.get('PERSONAL_DATA_DB_NAME')

    cnx = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )
    return cnx


def main():
    """
    Fonction principale qui récupère toutes les lignes de la table `users`
    et affiche chaque ligne sous un format filtré.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    logger = get_logger()

    for row in rows:
        row_str = "; ".join([f"{field}={value}" for field,
                             value in zip(PII_FIELDS,
                                          row)])
        logger.info(row_str)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
