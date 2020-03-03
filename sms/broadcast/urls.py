from django.urls import path
from .views import sms

urlpatterns = [
    path('sms/', sms),
]
