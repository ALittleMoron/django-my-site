from django.urls import path
from django.views.generic import RedirectView

from .views import (PostDelete, PostDetail, PostList, PostsByTagsList)

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='microblog/postList'), name='homePage'),
    path('microblog/', PostList.as_view(), name="microblog/postList"),
    path('microblog/post/<slug:slug>', PostDetail.as_view(), name='microblog/postDetail'),
    path('microblog/by-tag=<str:name>', PostsByTagsList.as_view(), name='microblog/postTags'),
    path('microblog/post/<slug:slug>/delete', PostDelete.as_view(), name='microblog/postDelete'),
]
