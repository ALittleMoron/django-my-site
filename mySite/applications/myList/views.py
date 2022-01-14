from random import choice
from typing import Any, Dict

from django.http.request import HttpRequest
from django.http.response import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.views.generic.base import ContextMixin, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from .models import Product, Rating, RatingItem


def random_redirect(request):
    to = ('series/', 'book/', 'film/', 'game/')
    return redirect(choice(to))


class ProductListView(ContextMixin, View):
    template_name = 'myList/myList.html'
    context_object_name = 'list'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        product = kwargs.get('product')
        verbosed = {'film': 'фильмов', 'game': 'игр', 'series': 'сериалов', 'book': 'книг'}
        if product not in verbosed:
            raise Http404
        context = self.get_context_data(
            title=f'Список {verbosed[product]}',
            dict_queryset = Product.objects.separated_by_status(product),
        )
        
        return render(request, self.template_name, context)


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'myList/productDetail.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context.update(self.get_object().rating.avarage_rating_score)
        
        return context


class RatingListView(ListView):
    model = Rating
    context_object_name = 'ratingItems'
    template_name = 'myList/productDetailRating.html'
    slug_url_kwarg = 'slug'


class ProductDelete(DeleteView):
    model = Product
    template_name = 'myList/productDelete.html'
    context_object_name = 'product'
    success_url = '/myList/'
