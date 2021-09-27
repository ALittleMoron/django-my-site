from django.urls import path

from .views import AboutMe, Resume, GitHubProjects


urlpatterns = [
    path('', Resume.as_view(), name='resume'),
    path('about-me/', AboutMe.as_view(), name='resume/aboutMe'),
    path('git-hub-projects/', GitHubProjects.as_view(), name='resume/gitHubProjects'),
]