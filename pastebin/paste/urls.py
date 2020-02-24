from django.urls import path
from .views import PasteCreate, PasteDetail, PasteList, PasteEdit, PasteDelete

urlpatterns = [
    path('', PasteCreate.as_view(), name='paste_create'),
    path('pastes/', PasteList.as_view(), name='paste_list'),
    path('paste/<int:pk>', PasteDetail.as_view(), name='paste_detail'),
    path('paste/delete/<int:pk>', PasteDelete.as_view(), name='paste_delete'),
    path('paste/edit/<int:pk>', PasteEdit.as_view(), name='paste_edit'),
]
