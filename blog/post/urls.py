from django.urls import path, include
from .views import PostWeekArchiveView, PostMonthArchiveView, add_post, view_post

urlpatterns = [
    path('<str:slug>', view_post, name='blog_post_detail'),
    path('add', add_post, name='blog_add_post'),
    path('archive/<int:year>/month/<int:month>', PostMonthArchiveView.as_view(), name='blog_archive_month'),
    path('archive/<int:year>/week/<int:week>', PostWeekArchiveView.as_view(), name='blog_archive_week'),
]