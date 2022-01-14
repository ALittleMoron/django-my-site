from django.contrib import admin
from django.contrib import messages
from django.utils.html import format_html
from django.utils.translation import ngettext
from django.templatetags.static import static
from nested_inline.admin import NestedTabularInline, NestedStackedInline, NestedModelAdmin

from .forms import RatingOnlyAdminForm, CKProductAdminForm
from .models import Product, Rating, RatingItem


class RatingItemsInline(NestedTabularInline):
    model = RatingItem
    extra = 1
    fk_name = 'parent'
    
    
class RatingInline(NestedStackedInline):
    model = Rating
    extra = 1
    fk_name = 'parent_product'
    inlines = [RatingItemsInline, ]


class RatingOnlyAdmin(admin.ModelAdmin):
    form = RatingOnlyAdminForm
    inlines = [RatingItemsInline,]


class CommonProductAdmin(NestedModelAdmin):
    form = CKProductAdminForm
    
    list_display = (
        "id",
        "product_type",
        "name",
        "native_name",
        "i_recommend",
        "is_published",
        "poster_preview_tag",
    )
    list_display_links = ("id", "name", "native_name")
    search_fields = ("name", "native_name")
    list_filter = ("i_recommend", "product_type")
    prepopulated_fields = {"slug": ("name",)}
    actions = ['make_published']
    inlines = [RatingInline, ]

    def poster_preview_tag(self, obj: Product):
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


admin.site.register(Product, CommonProductAdmin)
admin.site.register(Rating, RatingOnlyAdmin)