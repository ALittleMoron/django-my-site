from django.urls import path
from .views import HomePage, BlogList

urlpatterns = [
    path('', HomePage.as_view(), name='homePage'),
    path('microblog/', BlogList.as_view(), name="microblog/blogList")
]
