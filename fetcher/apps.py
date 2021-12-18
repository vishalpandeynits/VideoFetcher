from django.apps import AppConfig

class FetcherConfig(AppConfig):
    name = 'fetcher'
    def ready(self):
        from . import updater
        updater.start()