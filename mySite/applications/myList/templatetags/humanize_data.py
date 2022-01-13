from django import template

from myList.models import Product, PRODUCT_TYPE, RATING_CHOICES


register = template.Library()


@register.filter
def product_type_verbose(boundField):
    return list(filter(lambda x: x[0] == boundField, PRODUCT_TYPE))[0][1]


@register.filter
def rating_verbose(boundField):
    print(boundField, type(boundField))
    return list(filter(lambda x: x[0] == round(boundField), RATING_CHOICES))[0][1]


@register.filter
def starred(ratingField):
    return '★' * round(ratingField)


@register.filter
def not_starred(ratingField):
    return '★' * round(10 - ratingField)