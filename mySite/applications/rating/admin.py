from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import RatingItem


class RatingItemInline(GenericTabularInline):
    model = RatingItem
    extra = 0


class RatingItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'label', 'positive_offset', 'rating_purpose_type', 'score']
    list_display_link = ['id']
    list_filter = ['rating_purpose_type', 'score']
    readonly_fields = ['content_object']


admin.site.register(RatingItem, RatingItemAdmin)
