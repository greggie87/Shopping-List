from django.shortcuts import render
from django.views.generic.list import ListView
from .models import List

# Create your views here.

class ShoppingLists(ListView):
    model = List