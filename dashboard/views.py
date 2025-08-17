from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.http import  HttpResponse

def home(request):
    return HttpResponse("BI Dashboard is UP !!")