#!/usr/bin/env python3

""" User authentication module.
"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> str:
    """Hash a password and returns the hashed password.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate a new UUID and returns it.

    Returns:
        str: The generated UUID.
    """
    return str(uuid.uuid4())


class Auth:
    """Class for user authentication.
    """

    def __init__(self):
        """
        Initialize the Auth class by creating a new instance of the DB class.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user with the given email and password.

        Args:
            email (str): The email of the user to register.
            password (str): The password of the user to register.

        Returns:
            User: The newly registered User object.

        Raises:
            ValueError: If the user with the given email already exists.
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            new_user = self._db.add_user(email, _hash_password(password))
            return new_user
        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates login credentials.

        Args:
            email (str): The email of the user attempting to log in.
            password (str): The password of the user attempting to log in.

        Returns:
            bool: True if the login credentials are valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Creates a new session for the user with the given email.

        Args:
            email (str): The email of the user to create a session for.

        Returns:
            str: The session ID for the newly created session.

        Raises:
            None.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> str:
        """Gets the user associated with the given session ID.

        Args:
            session_id (str): The session ID to retrieve the user for.

        Returns:
            str: The User object associated with the given session ID,
            or None if no user is found.
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroy a user's session.

        Args:
            user_id (int): The ID of the user
            whose session should be destroyed.
        """
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """Generate a reset password token for a user.

        If the user does not exist, a ValueError will be raised.

        Args:
            email (str): The email of the user
            to generate a reset password token for.

        Returns:
            The reset password token.
        """
        try:
            user = self._db.find_user_by(email=email)
            reset_token = _generate_uuid()
            self._db.update_user(user.id, reset_token=reset_token)
            return reset_token
        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Update password with a reset token

        Args:
            reset_token (str): The reset token to verify user identity
            password (str): The new password to update for the user

        Raises:
            ValueError: If no user found with the given reset token

        """
        try:
            # Find the user with the given reset token
            user = self._db.find_user_by(reset_token=reset_token)
            # Update the user's hashed password with the new password
            self._db.update_user(user.id,
                                 hashed_password=_hash_password(password),
                                 reset_token=None)
        except NoResultFound:
            raise ValueError
