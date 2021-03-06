"""mySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar

from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('', RedirectView.as_view(pattern_name='microblog:list')),
    path('microblog/', include('microblog.urls', namespace='microblog')),
    path('about-me/', include('resume.urls')),
    path('myList/', include('myList.urls', namespace='myList')),
    path('rating/', include('rating.urls', namespace='rating')),
    path('api/v1/', include('api.urls', namespace='api')),
]


if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)