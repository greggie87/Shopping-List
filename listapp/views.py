from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from .models import List

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'listapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('lists')

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


class ListUpdate(UpdateView):
    model = List
    fields = ['title']
    success_url = reverse_lazy('lists')

class ListDelete(DeleteView):
    model = List
    context_object_name = 'list'
    success_url = reverse_lazy('lists')