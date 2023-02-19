#!/usr/bin/env python3
"""This module contains the DB class for managing database interactions."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class for managing database interactions."""

    def __init__(self):
        """Initialize the DB class and create a new database connection."""
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Create a new session if one does not already exist."""
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user to the database.

        Args:
            email (str): The email address of the user.
            hashed_password (str): The hashed password of the user.

        Returns:
            User: The newly created User object.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """Find a user in the database based on the given criteria.

        Args:
            **kwargs: The search criteria for finding the user.

        Returns:
            User: The User object that matches the search criteria.

        Raises:
            InvalidRequestError: If the search criteria is invalid.
            NoResultFound: If no matching user is found in the database.
        """
        try:
            record = self._session.query(User).filter_by(**kwargs).first()
        except TypeError:
            raise InvalidRequestError
        if record is None:
            raise NoResultFound
        return record

    def update_user(self, user_id: int, **kwargs) -> None:
        """Update the user with the given ID with the new data.

        Args:
            user_id (int): The ID of the user to be updated.
            **kwargs: The new data to update the user with.

        Raises:
            ValueError: If the new data is invalid
            or does not match any fields in the User model.
        """
        user_record = self.find_user_by(id=user_id)

        for key, value in kwargs.items():
            if hasattr(user_record, key):
                setattr(user_record, key, value)
            else:
                raise ValueError

        self._session.commit()
