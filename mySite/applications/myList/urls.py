from django.urls import path

from .views import (ProductDeleteView, ProductDetailView)


urlpatterns = [
    # path('', random_redirect, name='myList/randomRedirect'),
    # path('<str:model_name>/', ProductListView.as_view(), name='myList/choose'),
    path('<str:model_name>/<slug:slug>', ProductDetailView.as_view(), name='myList/productDetail'),
    path('<str:model_name>/<slug:slug>/delete', ProductDeleteView.as_view(), name='myList/productDelete'),
]