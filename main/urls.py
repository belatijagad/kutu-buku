from django.urls import path, include
from main.views import show_main
from main.views import login_user
from main.views import register
from main.views import logout_user
from main.views import login_moderator


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('autentikasi/', include('autentikasi.urls')),
    path('login_moderator/', login_moderator, name='login_moderator'),
]