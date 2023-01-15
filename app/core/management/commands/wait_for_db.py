"""Django commands to wait for the database to start properly
   and then start the app"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Dhango command to wait for database to start properly"""

    def handle(self, *args, **kwargs):
        ...
