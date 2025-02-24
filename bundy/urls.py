from django.urls import path
from django.shortcuts import redirect
from .views import (
    JacketListView,
    JacketCreateView,
    JacketDetailView,
    JacketUpdateView,
    JacketDeleteView,
    menu
)

urlpatterns = [
    path('', lambda request: redirect('sklad')),
    path('sklad/', JacketListView.as_view(), name='sklad'),
    path('vytvor/', JacketCreateView.as_view(), name='vytvor'),
    path('bundy/<int:pk>/', JacketDetailView.as_view(), name='jacket-detail'),
    path('bundy/<int:pk>/upravit/', JacketUpdateView.as_view(), name='jacket-update'),
    path('bundy/<int:pk>/vymazat/', JacketDeleteView.as_view(), name='jacket-delete'),
]
