from django.urls import path, include
from bookmark.views import show_main, show_json_by_id

app_name = 'daftar_membaca'

urlpatterns = [
    path('daftar-membaca', show_main, name='show_main'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]