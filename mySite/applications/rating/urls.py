from django.urls import path
from django.views.generic import RedirectView

from .views import ProductRatingView, RatingSystemView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='rating/ratingSystem'), name='rating/homePage'),
    path("rating-system", RatingSystemView.as_view(), name="rating/ratingSystem"),
    path(
        "<str:model_name>/<slug:slug>/",
        ProductRatingView.as_view(),
        name="rating/productDetailRating",
    ),
]
