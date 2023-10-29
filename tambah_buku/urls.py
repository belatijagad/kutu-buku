from django.urls import path, include
from tambah_buku.views import create_novel

app_name = 'tambah_buku'

urlpatterns = [
    path('tambah-buku', create_novel, name='create_novel'),
]