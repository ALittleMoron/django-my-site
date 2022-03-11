from django.urls import path
from django.views.generic import RedirectView

from .views import (PostDelete, PostDetail, PostList, PostsByTagsList)


app_name = 'microblog'

urlpatterns = [
    path('', PostList.as_view(), name="list"),
    path('post/<slug:slug>', PostDetail.as_view(), name='detail'),
    path('by-tag=<str:name>', PostsByTagsList.as_view(), name='tags'),
    path('post/<slug:slug>/delete', PostDelete.as_view(), name='delete'),
]
