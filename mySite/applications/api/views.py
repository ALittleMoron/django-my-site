from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from microblog.models import Post
from .serializers import PostSerializer


class PostAPIListOrCreateView(APIView):
    def get(self, request):
        posts = Post.objects.filter(is_published=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostAPIDetailOrUpdateView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serialiser = PostSerializer(post)
        return Response(serialiser.data)

    def patch(self, request, pk, partial=True):
        if request.user.is_superuser:
            post = get_object_or_404(Post, pk=pk)
            post_data = JSONParser().parse(request)
            serializer = PostSerializer(post, data=post_data, partial=partial)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(
            {"sucess": False, "detail": "permision denied (you are not super user)"}
        )

    def post(self, request, pk):
        return self.patch(request, pk, partial=False)

    def delete(self, request, pk):
        if request.user.is_superuser:
            post = get_object_or_404(Post, pk=pk)
            post.delete()
            return JsonResponse({"sucess": True})
        return JsonResponse(
            {"sucess": False, "detail": "permision denied (you are not super user)"}
        )
