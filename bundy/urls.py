from django.shortcuts import redirect
from django.urls import path
from bundy import views  # ✅ Správně
from .views import JacketListView, JacketCreateView

urlpatterns = [
    path('', lambda request: redirect('sklad/')),  # Přesměruje root URL na /sklad/
    path('sklad/', JacketListView.as_view(), name='sklad'),  # Nyní cesta /sklad/ volá náš ListView
    path('vytvor/', JacketCreateView.as_view(), name='vytvor'),  # Použijeme `CreateView`
    path('bundy/', JacketListView.as_view(), name='jacket-list'),  # Sklad
]
