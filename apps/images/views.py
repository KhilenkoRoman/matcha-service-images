from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import ImagesSerializer
from .models import Image


class ImageView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ImagesSerializer

    def get(self, request, *args, **kwargs):
        qs = Image.objects.filter(user_id=kwargs.get('user_id')).order_by('-date_created')
        return Response(data=self.get_serializer(qs, many=True).data, status=status.HTTP_200_OK)