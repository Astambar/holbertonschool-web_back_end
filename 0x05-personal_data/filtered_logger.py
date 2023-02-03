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


def get_db() -> connection.MySQLConnection:
    """_summary_

    Returns:
        connection.MySQLConnection: _description_
    """
    username = environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password = environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    host = environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    name = environ.get('PERSONAL_DATA_DB_NAME')
    return MySQLConnection(
        user=username,
        password=password,
        host=host,
        database=name
    )


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


def main():
    # Récupérer la base de données
    db = get_db()
    cursor = db.cursor()

    # Exécuter la requête SQL
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()

    # Récupérer le logger
    logger = get_logger()

    # Pour chaque résultat, créer un message de journalisation
    for result in results:
        fields = PII_FIELDS + ("ip", "last_login", "user_agent")
        values = [f"{field}={result[i]}" for i, field in enumerate(fields)]
        log_message = "; ".join(values)
        logger.info(log_message)


if __name__ == '__main__':
    main()
