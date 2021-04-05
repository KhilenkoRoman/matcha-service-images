import uuid
from django.db import models


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.UUIDField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    image = models.ImageField(null=True, upload_to='images/')
    thumbnail = models.ImageField(null=True, upload_to='thumbnails/')