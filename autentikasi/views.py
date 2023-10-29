from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# Create your views here.

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Redirect to a success page.
            return JsonResponse({
              "status": True,
              "message": "Log In Successful!",
              # Insert any extra data if you want to pass data to Flutter
              # show username and password
              "username": username,
              "password": password
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Login Failed, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
          "status": False,
          "message": "Login Failed, Check Your Password."
        }, status=401)

@csrf_exempt
def logout(request):
    logout(request)
    return JsonResponse({
      "status": True,
      "message": "Log Out Successful!"
    }, status=200)

@csrf_exempt
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username, password)
    user.save()
    return JsonResponse({
      "status": True,
      "message": "Registration Successful!!",
      "username": username,
      "password": password
    }, status=200)

