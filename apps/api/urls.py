from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from apps.images.views import ImageView

app_name = 'api'
urlpatterns = [
    path('images/', include('apps.images.urls')),
    path('test/', ImageView.as_view(), name='images'),
]
