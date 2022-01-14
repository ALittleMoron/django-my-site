from django.urls import path

from .views import random_redirect, ProductDetail, ProductListView, ProductDelete, RatingListView


urlpatterns = [
    path('', random_redirect, name='myList/randomRedirect'),
    # path('rating-system', ..., name='myList/ratingSystem),
    path('<str:product>/', ProductListView.as_view(), name='myList/choose'),
    path('product-detail/<slug:slug>', ProductDetail.as_view(), name='myList/productDetail'),
    path(
        'product-detail/<slug:slug>/rating-system',
        RatingListView.as_view(),
        name='myList/productDetailRating'
    ),
    path('product-detail/<slug:slug>/delete', ProductDelete.as_view(), name='myList/productDelete'),
]