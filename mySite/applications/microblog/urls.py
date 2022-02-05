from django.urls import path
from django.views.generic import RedirectView

from .views import (PostDelete, PostDetail, PostList, PostsByTagsList)


app_name = 'microblog'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='microblog:list'), name='homePage'),
    path('microblog/', PostList.as_view(), name="list"),
    path('microblog/post/<slug:slug>', PostDetail.as_view(), name='detail'),
    path('microblog/by-tag=<str:name>', PostsByTagsList.as_view(), name='tags'),
    path('microblog/post/<slug:slug>/delete', PostDelete.as_view(), name='delete'),
]
