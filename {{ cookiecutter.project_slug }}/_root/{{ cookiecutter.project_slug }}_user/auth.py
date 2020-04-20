"""Define a Backend for settings based super user credentials."""
from django.conf import settings

from .models import User


class SettingsBackend:
    """
    Authenticate against the settings ADMIN_USER and ADMIN_PASSWORD.

    For example:

    ADMIN_USER = 'admin'
    ADMIN_PASSWORD = 'password'
    """

    @staticmethod
    def authenticate(request, username=None, password=None):
        """
        Check credentials from settings and return the user.

        If a user with the given username does not exist, create one.
        """
        if not settings.ADMIN_USER or not settings.ADMIN_PASSWORD:
            return None

        login_valid = settings.ADMIN_USER == username
        pwd_valid = settings.ADMIN_PASSWORD == password

        if not login_valid or not pwd_valid:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Create a new user. There's no need to set a password
            # because only the password from settings.py is checked.
            user = User.objects.create_superuser(username=username, email=None, password=None)
        return user

    @staticmethod
    def get_user(user_id):
        """Return the user for the given ID, or None if does not exist."""
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
