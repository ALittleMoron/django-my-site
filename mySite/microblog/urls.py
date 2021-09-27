from django.urls import path

from .views import (HomePage, PostCreate, PostDelete, PostDetail, PostList,
                    PostUpdate)

urlpatterns = [
    path('', HomePage.as_view(), name='homePage'),
    path('microblog/', PostList.as_view(), name="microblog/postList"),
    path('microblog/post/create', PostCreate.as_view(), name='microblog/postCreate'),
    path('microblog/post/<slug:slug>', PostDetail.as_view(), name='microblog/postDetail'),
    path('microblog/post/<slug:slug>/update', PostUpdate.as_view(), name='microblog/postUpdate'),
    path('microblog/post/<slug:slug>/delete', PostDelete.as_view(), name='microblog/postDelete'),
]
