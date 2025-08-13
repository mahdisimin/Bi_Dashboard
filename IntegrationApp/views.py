from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home (request):
    #return HttpResponse("Hello, world. You're at the polls page.")
    return  render(request, 'IntegrationApp/home.html')