from random import choice
from django.shortcuts import redirect
from django.views.generic.list import ListView

from .models import Product


def random_redirect(request):
    to = ('series/', 'book/', 'film/', 'game/')
    return redirect(choice(to))


class MyModelsListView(ListView):
    template_name = 'myList/myList.html'
    context_object_name = 'list'


class BookList(MyModelsListView):
    queryset = Product.objects.filter(product_type='book')


class FilmList(MyModelsListView):
    queryset = Product.objects.filter(product_type='film')


class SeriesList(MyModelsListView):
    queryset = Product.objects.filter(product_type='series')


class GameList(MyModelsListView):
    queryset = Product.objects.filter(product_type='game')