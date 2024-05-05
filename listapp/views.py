from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import List

# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'listapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('lists')


class ShoppingLists(LoginRequiredMixin, ListView):
    model = List
    context_object_name = 'lists'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lists'] = context['lists'].filter(user=self.request.user)
        return context


class ListDetail(LoginRequiredMixin, DetailView):
    model = List
    context_object_name = 'uniquelist'


class ListCreate(LoginRequiredMixin, CreateView):
    model = List
    fields = ['title']
    success_url = reverse_lazy('lists')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ListCreate, self).form_valid(form)


class ListUpdate(LoginRequiredMixin, UpdateView):
    model = List
    fields = ['title']
    success_url = reverse_lazy('lists')


class ListDelete(LoginRequiredMixin, DeleteView):
    model = List
    context_object_name = 'list'
    success_url = reverse_lazy('lists')