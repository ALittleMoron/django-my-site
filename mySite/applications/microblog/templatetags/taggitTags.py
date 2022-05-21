from collections import Counter

from django import template
from django.contrib.contenttypes.models import ContentType
from taggit.models import TaggedItem

from microblog.models import Post


register = template.Library()


@register.simple_tag()
def get_most_popular_tags() -> list[tuple[str, int]]:
    tags = TaggedItem.objects.filter(
        content_type=ContentType.objects.get_for_model(Post)
    ).filter(tag__post__is_published=True)
    return Counter(map(lambda item: item.tag, tags)).most_common(10)
