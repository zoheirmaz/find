from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login

def my(request):
    if request.user.is_authenticated():

