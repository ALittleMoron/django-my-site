from django.contrib import admin, messages
from django.templatetags.static import static
from django.utils.html import format_html
from django.utils.translation import ngettext

from .forms import (CKAnimeAdminForm, CKBookAdminForm, CKFilmAdminForm, CKGameAdminForm,
                    CKSeriesAdminForm)
from .models import Anime, Book, Film, Game, Series
from rating.admin import RatingItemInline


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "i_recommend",
        "is_published",
        "poster_preview_tag",
    )
    list_display_links = ("id", "name",)
    search_fields = ("name",)
    list_filter = ("i_recommend",)
    prepopulated_fields = {"slug": ("name",)}
    actions = ['make_published']
    inlines = [RatingItemInline,]

    def poster_preview_tag(self, obj):
        image = '<img src="{}" width="45px" height="45px"/>'
        if not obj.poster:
            return format_html(
                image.format(static('dummy.png'))
            )
        return format_html(
            image.format(obj.poster.url)
        )
    
    def make_published(self, request, queryset):
        updated = queryset.update(is_published=True)
        self.message_user(request, ngettext(
            '%d тайтл был успешно опубликован.',
            '%d тайтлов были успешно опубликованы.',
            updated,
        ) % updated, messages.SUCCESS)

    poster_preview_tag.allow_tags = True
    poster_preview_tag.short_description = 'Превью'
    
    make_published.short_description = 'Опубликовать выделенное'


class AnimeAdmin(ProductAdmin):
    form = CKAnimeAdminForm


class BookAdmin(ProductAdmin):
    form = CKBookAdminForm


class FilmAdmin(ProductAdmin):
    form = CKFilmAdminForm


class GameAdmin(ProductAdmin):
    form = CKGameAdminForm


class SeriesAdmin(ProductAdmin):
    form = CKSeriesAdminForm


admin.site.register(Anime, AnimeAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Series, SeriesAdmin)
