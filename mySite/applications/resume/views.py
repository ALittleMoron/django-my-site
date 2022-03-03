from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import View

from .models import GitHubRepositoryCard


class Resume(View):
    http_method_names = ['get']
    template_name = 'resume/resume.html'
    
    def get(self, request: HttpRequest) -> HttpResponse:
        cards = GitHubRepositoryCard.objects.filter(is_published=True).all()
        return render(request, self.template_name, {'cards': cards})
