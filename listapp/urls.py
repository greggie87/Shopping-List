from django.urls import path
from .views import ShoppingLists

urlpatterns = [
    path('', ShoppingLists.as_view(), name='lists'),
]