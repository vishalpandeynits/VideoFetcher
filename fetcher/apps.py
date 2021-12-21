from django.apps import AppConfig
import sys

class FetcherConfig(AppConfig):
    name = 'fetcher'
    def ready(self):
        if 'runserver' in sys.argv:
            """
                Not to run updater when any command other than runserver is running.
                It is done to avoid record creation in database while `migrate` is running 
                and has already acquired the database's lock.
                #TODO: migrate to better solution.
            """
            from . import updater
            updater.start()