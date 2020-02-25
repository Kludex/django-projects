from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import login

urlpatterns = [
    path('accounts/login/', login),
    path('admin/', admin.site.urls),
    path('post/', include('post.urls')),
]
