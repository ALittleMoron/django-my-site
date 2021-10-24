from django.urls import path

from .views import random_redirect, ProductDetail, ProductListView


urlpatterns = [
    path('', random_redirect, name='myList/randomRedirect'),
    path('<str:product>/', ProductListView.as_view(), name='myList/choose'),
    path('product-detail/<slug:slug>', ProductDetail.as_view(), name='myList/productDetail'),
]