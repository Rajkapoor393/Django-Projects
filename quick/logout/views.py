from django.shortcuts import render, redirect
from django.contrib import auth


# Create your views here.
def logout1(request):
    auth.logout(request)
    return redirect('/')
