from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "users/index.html")

def register(request):
    return render(request, "users/register.html")

def login(request):
    return render(request, "users/login.html")

def logout(request):
    return HttpResponse("Logout done...")
