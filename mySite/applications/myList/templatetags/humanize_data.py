from django import template

from myList.models import Product


register = template.Library()


@register.filter
def product_type_verbose(boundField):
    return list(filter(lambda x: x[0] == boundField, Product.PRODUCT_TYPE))[0][1]


@register.filter
def rating_verbose(boundField):
    return list(filter(lambda x: x[0] == boundField, Product.RATING_CHOICES))[0][1]


@register.filter
def rating_like_stars_inline(ratingField):
    return '★' * ratingField


@register.filter
def not_starred(ratingField):
    return '★' * (10 - ratingField)