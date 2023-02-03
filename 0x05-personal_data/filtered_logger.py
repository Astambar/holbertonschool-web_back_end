#!/usr/bin/env python3
"""_summary_

Returns:
    _type_: _description_
"""
import logging
import re
import typing
import os
import mysql.connector
List = typing.List
PII_FIELDS = ("name", "email", "phone", "ssn", "password")
environ = os.environ
connection = mysql.connector.connection
MySQLConnection = connection.MySQLConnection


def get_db():
    """_summary_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    username = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    database = environ.get("PERSONAL_DATA_DB_NAME")
    if not database:
        raise ValueError(
            "Environment variable 'PERSONAL_DATA_DB_NAME' must be set")
    return MySQLConnection(user=username,
                           password=password,
                           host=host,
                           database=database)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ filter_datum function """
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """_summary_

        Args:
            record (logging.LogRecord): _description_

        Returns:
            str: _description_
        """
        filtered_message = filter_datum(self.fields, self.REDACTION,
                                        record.getMessage(), self.SEPARATOR)
        record.msg = filtered_message
        return super().format(record)


def get_logger() -> logging.Logger:
    """_summary_

    Returns:
        logging.Logger: _description_
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    formatter = RedactingFormatter(PII_FIELDS)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
