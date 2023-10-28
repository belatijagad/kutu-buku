from django.urls import path
from . import views

app_name = 'halaman_buku'

urlpatterns = [
    path('buku/<int:book_id>/', views.buku_detail, name='buku_detail'),
]
