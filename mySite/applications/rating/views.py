from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic.list import ListView

from .models import RatingItem


class RatingSystemView(View):
    template_name = 'rating/ratingSystem.html'
    http_method_names = ['get']
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProductRatingView(View):
    context_object_name = 'ratingItems'
    http_method_names = ['get']
    template_name = 'rating/productDetailRating.html'
