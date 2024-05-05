from django.urls import path
from .views import ShoppingLists, ListDetail, ListCreate

urlpatterns = [
    path('', ShoppingLists.as_view(), name='lists'),
    path('list/<int:pk>/', ListDetail.as_view(), name='list'),
    path('list-create/', ListCreate.as_view(), name='list-create'),
]