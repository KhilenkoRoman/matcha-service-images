from django.apps import AppConfig
from .consumers import ImagesConsumer


class ImagesConfig(AppConfig):
    name = 'apps.images'

    def ready(self):
        consumer = ImagesConsumer()
        consumer.daemon = True
        consumer.start()
