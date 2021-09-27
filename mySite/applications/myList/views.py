from random import choice
from typing import List
from django.shortcuts import redirect, render
from django.views.generic.list import ListView


def random_redirect(request):
    to = ('anime/', 'book/', 'film/', 'game/')
    return redirect(choice(to))


class AnimeList(ListView):
    pass


class BookList(ListView):
    pass


class FilmList(ListView):
    pass


class GameList(ListView):
    pass