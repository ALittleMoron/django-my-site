from django.urls import path

from .views import random_redirect, AnimeList, BookList, FilmList, GameList


urlpatterns = [
    path('', random_redirect, name='myList/randomRedirect'),
    path('anime/', AnimeList.as_view(), name='myList/animeList'),
    path('book/', BookList.as_view(), name='myList/booksList'),
    path('film/', FilmList.as_view(), name='myList/filmList'),
    path('game/', GameList.as_view(), name='myList/gameList'),
]