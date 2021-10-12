from random import choice
from typing import List
from django.shortcuts import redirect, render
from django.views.generic.list import ListView

from .models import Film, Series


def random_redirect(request):
    to = ('series/', 'book/', 'film/', 'game/')
    return redirect(choice(to))


class BookList(ListView):
    pass


class FilmList(ListView):
    template_name = 'myList/films.html'
    queryset = Film.objects.all()


class SeriesList(ListView):
    template_name = 'myList/series.html'
    queryset = Series.objects.all()


class GameList(ListView):
    pass