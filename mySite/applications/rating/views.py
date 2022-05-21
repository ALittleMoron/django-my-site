from django.shortcuts import render
from django.views.generic.base import View

from myList.mixins import ModelNameDispatchMixin
from .models import RatingItem


class RatingSystemView(View):
    template_name = "rating/ratingSystem.html"
    http_method_names = ["get"]

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ProductRatingView(ModelNameDispatchMixin, View):
    http_method_names = ["get"]
    template_name = "rating/productDetailRating.html"

    def get(self, request, *args, **kwargs):
        self.objects = RatingItem.objects.filter(
            object_id=self.kwargs.get("pk")
        ).separated_by_purpose_type()
        context = {
            "dict_queryset": self.objects,
            "goback_model": self.model._meta.model_name,
            "goback_slug": self.model.objects.get(pk=self.kwargs.get("pk")).slug,
        }
        return render(request, self.template_name, context)
