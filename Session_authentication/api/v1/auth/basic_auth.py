#!/usr/bin/env python3
""" BasicAuth  module
"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar, Tuple
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth  class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ extract_base64_authorization_header method
        """
        if authorization_header is None or not \
            isinstance(authorization_header, str) or not \
                authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) \
            -> str:
        """ decode_base64_authorization_header method
        """
        if base64_authorization_header is None or not \
           isinstance(base64_authorization_header, str):
            return None
        try:
            return base64.b64decode(base64_authorization_header)\
                .decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                     str) -> Tuple[str, str]:
        """ extract_user_credentials method
        """
        if decoded_base64_authorization_header is None or not \
            isinstance(decoded_base64_authorization_header, str) or ':' not \
                in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email: str, user_pwd: str)\
            -> TypeVar('User'):
        """ user_object_from_credentials method
        """
        if user_email is None or \
            user_pwd is None or not\
                isinstance(user_email, str) or not\
                isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ current_user method
        """
        authorization_header = \
            self.authorization_header(request)
        base64_authorization_header = self.\
            extract_base64_authorization_header(authorization_header)
        decoded_base64_authorization_header = self.\
            decode_base64_authorization_header(base64_authorization_header)
        user_email, user_pwd = self.\
            extract_user_credentials(decoded_base64_authorization_header)
        return self.user_object_from_credentials(user_email, user_pwd)
