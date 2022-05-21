from django.urls import path
from .views import PostAPIDetailOrUpdateView, PostAPIListOrCreateView


app_name = "api"

urlpatterns = [
    path("posts", PostAPIListOrCreateView.as_view(), name="post-list"),
    path("posts/<int:pk>", PostAPIDetailOrUpdateView.as_view(), name="post-detail"),
]
