from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import (View, ListView, CreateView, UpdateView, DeleteView, DetailView)

from .forms import PostForm
from .mixins import NotNavigate
from .models import Post


class Resume(View):
    http_method_names = ['get']
    template_name = 'microblog/resume.html'
    
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)



class HomePage(View):
    """ Класс вывода домашней страницы.
    
    Особо ничего не делает. Только выводит приветственную страницу с навигацией по сайту.
    """
    http_method_names = ['get']
    template_name = 'microblog/homePage.html'
    
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, self.template_name)


class PostList(ListView):
    template_name = 'microblog/postList.html'
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


class PostDetail(NotNavigate, DetailView):
    model = Post
    template_name = 'microblog/postDetail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'


class PostCreate(NotNavigate, LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'microblog/postCreate.html'


    def post(self, request, *args, **kwargs):
        """ Переопределенный метод клааса CreateView для отправки сообщения об
        ошибки валидации формы.
        """
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            messages.error('Некорректные данные в форме!')
            return self.form_invalid(form)


class PostUpdate(NotNavigate, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'microblog/postUpdate.html'


class PostDelete(NotNavigate, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'microblog/postDelete.html'
    context_object_name = 'post'
    success_url = '/microblog/'