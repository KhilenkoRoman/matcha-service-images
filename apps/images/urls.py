from django.urls import path
from .views import ImageView

app_name = 'users'
urlpatterns = [
    path('<uuid:user_id>/', ImageView.as_view(), name='images'),
]
