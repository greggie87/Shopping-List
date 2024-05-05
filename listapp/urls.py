from django.urls import path
from .views import ShoppingLists, ListDetail, ListCreate, ListUpdate, ListDelete

urlpatterns = [
    path('', ShoppingLists.as_view(), name='lists'),
    path('list/<int:pk>/', ListDetail.as_view(), name='list'),
    path('list-create/', ListCreate.as_view(), name='list-create'),
    path('list-update/<int:pk>/', ListUpdate.as_view(), name='list-update'),
    path('list-delete/<int:pk>/', ListDelete.as_view(), name='list-delete'),
]