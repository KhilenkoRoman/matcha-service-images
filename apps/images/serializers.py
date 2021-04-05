from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Image
from django.conf import settings


class ImagesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    thumbnail = serializers.SerializerMethodField()

    def get_image(self, obj):
        if obj.image:
            return settings.BASE_URL + obj.image.url
        else:
            return None

    def get_thumbnail(self, obj):
        if obj.thumbnail:
            return settings.BASE_URL + obj.thumbnail.url
        else:
            return None

    class Meta:
        model = Image
        fields = ('id', 'date_created', 'date_updated', 'image', 'thumbnail',)