from django.urls import path
from .views import ShoppingLists, ListDetail

urlpatterns = [
    path('', ShoppingLists.as_view(), name='lists'),
    path('list/<int:pk>/', ListDetail.as_view(), name='list'),
]