from django.urls import include, path
from autentikasi.views import (
    register,
    login_user,
    logout_user,
)


app_name = 'autentikasi'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
]