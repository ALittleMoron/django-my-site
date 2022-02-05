from django.urls import path

from .views import (random_redirect, ProductDeleteView, ProductDetailView, ProductListView)


app_name = 'myList'

urlpatterns = [
    path('', random_redirect, name='randomRedirect'),
    path('<str:model_name>/', ProductListView.as_view(), name='choose'),
    path('<str:model_name>/<slug:slug>', ProductDetailView.as_view(), name='detail'),
    path('<str:model_name>/<slug:slug>/delete', ProductDeleteView.as_view(), name='delete'),
]