from django.urls import path, include
from . import views

app_name = 'tambah_buku'

urlpatterns = [
    path('', views.add_book, name='add_book'),
]