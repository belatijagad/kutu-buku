from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from main.models import UserProfile
from django.contrib.auth import get_user_model
from halaman_buku.models import Book

# @login_required(login_url='main:login')
# @login_required(login_url='/login')
def show_main(request):
    return render(request, 'main.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if role == 'moderator':
                return redirect('main:login_moderator')
            else:
                # Create UserProfile if it does not exist
                UserProfile.objects.get_or_create(user=user)
                login(request, user)
                return HttpResponseRedirect(reverse('main:show_main'))
        else:
            messages.error(request, 'Kredensial yang dimasukkan tidak cocok!')
            return redirect('main:login')

    context = {}
    return render(request, 'login.html', context)

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')

        if password != confirm_password:
            messages.error(request, 'Kata Sandi dan Konfirmasi Kata Sandi Tidak Cocok')
            return redirect('main:register')

        # Proses registrasi jika kata sandi cocok
        try:
            user = User.objects.create_user(username=username, password=password)
            user_profile = UserProfile.objects.create(user=user, role=role)
            return redirect('main:login')  # Ubah redirect ke halaman login
        except Exception as e:
            return redirect('main:register')
    
    return render(request, 'register.html')


@csrf_exempt
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_main'))
    response.delete_cookie('last_login')
    return response

def login_moderator(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Get user instance without checking password
        user = get_user_model().objects.filter(username=username).first()
        if user is None:
            login(request, user)
            return HttpResponseRedirect(reverse('main:show_main'))
        else:
            return redirect('main:login_moderator')

    context = {}
    return render(request, 'login_moderator.html', context)
