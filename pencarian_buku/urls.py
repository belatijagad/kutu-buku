from django.urls import path, include
from main.views import show_main
from pencarian_buku.views import pencarian_buku, cari_buku

app_name = 'pencarian_buku'

urlpatterns = [
    path('', pencarian_buku, name='pencarian_buku'),
    path('search/', cari_buku, name='cari_buku'),
]