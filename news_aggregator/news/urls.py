from django.urls import path

from .views import scrape, new_list

urlpatterns = [
    path('scrape/', scrape, name='scrape'),
    path('', new_list, name='home'),
]
