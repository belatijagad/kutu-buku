from django.urls import path
from . import views

app_name = 'halaman_buku'

urlpatterns = [
    path('<str:sha256sum>/', views.buku_detail, name='buku_detail'),
    path('tambah_ulasan/', views.tambah_ulasan, name='tambah_ulasan'),
]
