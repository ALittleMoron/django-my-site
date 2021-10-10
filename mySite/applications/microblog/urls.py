from django.urls import path

from .views import (HomePage, PostDelete, PostDetail, PostList, PostsByTagsList)

urlpatterns = [
    path('', HomePage.as_view(), name='homePage'),
    path('microblog/', PostList.as_view(), name="microblog/postList"),
    path('microblog/post/<slug:slug>', PostDetail.as_view(), name='microblog/postDetail'),
    path('microblog/by-tag=<str:name>', PostsByTagsList.as_view(), name='microblog/postTags'),
    path('microblog/post/<slug:slug>/delete', PostDelete.as_view(), name='microblog/postDelete'),
]
