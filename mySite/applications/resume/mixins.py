from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import View


class GetView(View):
    http_method_names = ['get']
    
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)
