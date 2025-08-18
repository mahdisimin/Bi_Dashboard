from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.http import  HttpResponse

def home(request):
    return render(request, 'dashboard/home.html')

def about(request):
    return render(request, 'dashboard/about.html')

