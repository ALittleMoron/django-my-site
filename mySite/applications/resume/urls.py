from django.urls import path

from .views import Resume, GitHubProjects


urlpatterns = [
    path('', Resume.as_view(), name='resume'),
    path('git-hub-projects/', GitHubProjects.as_view(), name='resume/gitHubProjects'),
]