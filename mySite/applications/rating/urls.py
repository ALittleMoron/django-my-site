from django.urls import path
from django.views.generic import RedirectView

from .views import ProductRatingView, RatingSystemView


app_name = 'rating'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='rating:ratingSystem'), name='homePage'),
    path("rating-system", RatingSystemView.as_view(), name="ratingSystem"),
    path(
        "<str:model_name>/<int:pk>/",
        ProductRatingView.as_view(),
        name="detail",
    ),
]
