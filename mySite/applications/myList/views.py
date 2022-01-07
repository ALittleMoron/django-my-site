from random import choice
from typing import Any

from django.http.request import HttpRequest
from django.http.response import HttpResponse, Http404
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from .models import Product
from applications.microblog.mixins import NoNavbar


def random_redirect(request):
    to = ('series/', 'book/', 'film/', 'game/')
    return redirect(choice(to))


class ProductListView(ListView):
    template_name = 'myList/myList.html'
    context_object_name = 'list'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        product = kwargs.get('product')
        if product not in {'film', 'game', 'series', 'book'}:
            raise Http404
        self.queryset = Product.objects.filter(product_type=product)
        return super().get(request, *args, **kwargs)


class ProductDetail(NoNavbar, DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'myList/productDetail.html'
    slug_url_kwarg = 'slug'


class ProductDelete(NoNavbar, DeleteView):
    model = Product
    template_name = 'myList/productDelete.html'
    context_object_name = 'product'
    success_url = '/myList/'
