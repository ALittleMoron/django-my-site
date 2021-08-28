from django.urls import path
from .views import HomePage, PostDelete, PostDetail, PostList, PostCreate, PostUpdate, Resume

urlpatterns = [
    path('', HomePage.as_view(), name='homePage'),
    path('microblog/', PostList.as_view(), name="microblog/postList"),
    path('microblog/post/<int:pk>', PostDetail.as_view(), name='microblog/postDetail'),
    path('microblog/post/create', PostCreate.as_view(), name='microblog/postCreate'),
    path('microblog/post/<int:pk>/update', PostUpdate.as_view(), name='microblog/postUpdate'),
    path('microblog/post/<int:pk>/delete', PostDelete.as_view(), name='microblog/postDelete'),
    path('resume/', Resume.as_view(), name='resume')
]
