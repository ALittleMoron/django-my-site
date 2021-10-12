from django.urls import path

from .views import random_redirect, SeriesList, BookList, FilmList, GameList


urlpatterns = [
    path('', random_redirect, name='myList/randomRedirect'),
    path('series/', SeriesList.as_view(), name='myList/animeList'),
    path('book/', BookList.as_view(), name='myList/booksList'),
    path('film/', FilmList.as_view(), name='myList/filmList'),
    path('game/', GameList.as_view(), name='myList/gameList'),
]