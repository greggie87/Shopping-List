from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list_app(request):
    return HttpResponse("Hello, This will be a shopping list app!")