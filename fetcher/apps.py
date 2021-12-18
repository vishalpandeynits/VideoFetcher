from django.apps import AppConfig
import sys

class FetcherConfig(AppConfig):
    name = 'fetcher'
    def ready(self):
        if 'runserver' in sys.argv:
            """
                Not to run updater when any command other than runserver is running.
                to avoid record creation in database while `migrate` has already acquired the database's lock.
            """
            from . import updater
            updater.start()