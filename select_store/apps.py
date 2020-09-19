from django.apps import AppConfig


class SelectStoreConfig(AppConfig):
    name = 'select_store'


    def ready(self):
        import select_store.signals.handlers # noqa
