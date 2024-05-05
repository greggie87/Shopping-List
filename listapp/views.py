from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import List

# Create your views here.

class ShoppingLists(ListView):
    model = List
    context_object_name = 'lists'


class ListDetail(DetailView):
    model = List
    context_object_name = 'uniquelist'


class ListCreate(CreateView):
    model = List
    fields = ['title']
    success_url = reverse_lazy('lists')