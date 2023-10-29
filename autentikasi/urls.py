from django.urls import include, path
from autentikasi.views import login
from autentikasi.views import logout
from autentikasi.views import register


app_name = 'autentikasi'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]