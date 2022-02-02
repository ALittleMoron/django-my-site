from random import choice
from typing import Any, Dict

from django.http.request import HttpRequest
from django.http.response import HttpResponse, Http404
from django.shortcuts import redirect, render
from django.views.generic.base import ContextMixin, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView

from . mixins import ModelNameDispatchMixin

def random_redirect(request):
    to = ('series/', 'book/', 'film/', 'game/')
    return redirect(choice(to))


class ProductListView(ModelNameDispatchMixin, ContextMixin, View):
    template_name = 'myList/myList.html'

    def get(self, request, *args, **kwargs):
        verbosed = {'film': 'фильмов', 'game': 'игр', 'series': 'сериалов', 'book': 'книг', 'anime': 'аниме'}
        context = self.get_context_data(
            title=f'Список {verbosed[self.model._meta.model_name]}',
            dict_queryset = self.model.objects.separated_by_status(),
        )
        
        return render(request, self.template_name, context)


class ProductDetailView(ModelNameDispatchMixin, DetailView):
    context_object_name = 'product'
    template_name = 'myList/productDetail.html'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return self.model.objects.annotate_avg_p_rate()
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object, title=self.object.name)
        return self.render_to_response(context)


class ProductDeleteView(ModelNameDispatchMixin, DeleteView):
    template_name = 'myList/productDelete.html'
    context_object_name = 'product'
    success_url = '/myList/'
