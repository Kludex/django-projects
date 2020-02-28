from django.urls import path
from .views import CityCreateView, CityDeleteView

urlpatterns = [
    path('', CityCreateView.as_view(), name='core'),
    path('delete/<int:pk>', CityDeleteView.as_view(), name='delete_city'),
]