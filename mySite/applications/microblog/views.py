from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView

from .models import Post


class PostList(ListView):
    template_name = "microblog/postList.html"
    model = Post
    context_object_name = "posts"
    paginate_by = 12

    def post(self, request: HttpRequest) -> HttpResponse:
        """Переопределенный метод класса ListView для обработки поиска по
        названию поста и тэгам.
        """
        search = request.POST.get("search")
        query = Post.objects.filter(Q(title__icontains=search) | Q(tags__name=search))
        return render(request, self.template_name, context={"posts": query})


class PostsByTagsList(PostList):
    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs["name"])


class PostDetail(DetailView):
    model = Post
    template_name = "microblog/postDetail.html"
    context_object_name = "post"
    slug_url_kwarg = "slug"


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "microblog/postDelete.html"
    context_object_name = "post"
    success_url = "/microblog/"
