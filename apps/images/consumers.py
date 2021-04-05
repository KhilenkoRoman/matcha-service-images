import base64
import json
import threading
from io import BytesIO

import pika
from PIL import Image as PilImage
from django.conf import settings
from django.core.files import File
from django.core.files.base import ContentFile


class ImagesConsumer(threading.Thread):
    def callback(self, ch, method, properties, body):
        from apps.images.models import Image
        data = json.loads(body)
        image_qs = Image.objects.create(user_id=data.get('user_id'))

        image = ContentFile(base64.b64decode(data.get('image')))

        thumbnail = PilImage.open(image)
        main_image = PilImage.open(image)

        h = thumbnail.height
        w = thumbnail.width

        if w == h:
            pass
        else:
            if w > h:
                y1 = 0
                y2 = h
                x1 = (w - h) / 2
                x2 = (w + h) / 2
            else:
                x1 = 0
                x2 = w
                y1 = (h - w) / 2
                y2 = (h + w) / 2
            thumbnail = thumbnail.crop((x1, y1, x2, y2))
        thumbnail = thumbnail.resize((200, 200))

        thumbnail_io = BytesIO()
        thumbnail.save(thumbnail_io, format='webp', quality=60)
        thumbnail_file = File(thumbnail_io)
        image_qs.thumbnail.save(f'{image_qs.id}.webp', thumbnail_file)

        main_image_io = BytesIO()
        main_image.save(main_image_io, format='webp', quality=80)
        main_image_file = File(main_image_io)
        image_qs.image.save(f'{image_qs.id}.webp', main_image_file)

    def run(self):
        credentials = pika.PlainCredentials(settings.RABBIT_USER, settings.RABIT_PASSWORD)
        parameters = pika.ConnectionParameters(settings.RABBIT_URL, settings.RABBIT_PORT, '/', credentials)
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()

        channel.exchange_declare(exchange='images', exchange_type='fanout')
        result = channel.queue_declare(queue='images_download')
        queue_name = result.method.queue

        channel.queue_bind(exchange='images', queue=queue_name)

        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=queue_name, on_message_callback=self.callback, auto_ack=True)
        channel.start_consuming()
