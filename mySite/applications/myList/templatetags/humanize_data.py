from django import template
from django.urls import reverse

from rating.models import RATING_CHOICES


register = template.Library()


@register.simple_tag
def url_to_edit_object(obj):
    return reverse(
        f"admin:{obj._meta.app_label}_{obj._meta.model_name}_change", args=[obj.pk]
    )


@register.filter
def model_name(obj):
    return obj._meta.model_name


@register.filter
def object_verbose_name(obj):
    return obj._meta.verbose_name


@register.filter
def rating_verbose(boundField):
    print(boundField, type(boundField))
    return list(filter(lambda x: x[0] == round(boundField), RATING_CHOICES))[0][1]


@register.filter
def starred(ratingField):
    return "★" * round(ratingField)


@register.filter
def not_starred(ratingField):
    return "★" * round(10 - ratingField)
