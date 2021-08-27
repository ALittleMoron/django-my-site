from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import (View, ListView, CreateView, UpdateView, DeleteView, DetailView)
from .models import Post

class HomePage(View):
    """ Класс вывода домашней страницы.
    
    Особо ничего не делает. Только выводит приветственную страницу с навигацией по сайту.
    """
    http_method_names = ['get']
    template_name = 'microblog/homePage.html'
    
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return render(request, self.template_name)


class BlogList(ListView):
    template_name = 'microblog/blogList.html'
    queryset = Post.objects.filter(is_published=True).all()
    context_object_name = 'posts'
    paginate_by = 12

    def post(self, request: HttpRequest) -> HttpResponse:
        """ Переопределенный метод класса ListView для обработки поиска по
        названию поста и тэгам.
        """
        search = request.POST.get('search')
        query = Post.objects.filter(
            Q(is_published=True),
            Q(title__icontains=search) | Q(tags__name=search)
        )
        return render(request, self.template_name, context={'posts': query})


class PostDetail(DetailView):
    pass


class PostCreate(LoginRequiredMixin, CreateView):
    pass


class PostUpdate(LoginRequiredMixin, UpdateView):
    pass


class PostDelete(LoginRequiredMixin, DeleteView):
    pass