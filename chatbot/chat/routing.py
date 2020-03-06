from django.urls import path

from .consumers import ChatConsumer


websockets_urlpatters = [
    path('ws/<str:room_name>/', ChatConsumer),
]