from django.utils.html import strip_tags
from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer

from microblog.models import Post


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["text"] = strip_tags(instance.text)
        return data

    class Meta:
        model = Post
        fields = "__all__"
