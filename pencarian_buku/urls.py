from django.urls import path, include
from main.views import show_main
from pencarian_buku.views import pencarian_buku, search_all

app_name = 'pencarian_buku'

urlpatterns = [
    path('cari-buku/', pencarian_buku, name='pencarian_buku'),
    path('mencari/', search_all, name='mencari_buku'),
]