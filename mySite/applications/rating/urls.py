from django.urls import path

from .views import ProductRatingView, RatingSystemView

urlpatterns = [
    path("rating-system", RatingSystemView.as_view(), name="rating/ratingSystem"),
    path(
        "<str:model_name>/<slug:slug>/",
        ProductRatingView.as_view(),
        name="rating/productDetailRating",
    ),
]
