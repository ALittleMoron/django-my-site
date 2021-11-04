from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.utils.html import format_html

from .models import Product


class CKProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget,
            'opinion': CKEditorWidget
        }


class CommonAdmin(admin.ModelAdmin):
    form = CKProductAdminForm
    
    list_display = (
        "id",
        "product_type",
        "name",
        "native_name",
        "rating",
        "i_recommend",
        "poster_preview_tag",
    )
    list_display_links = ("id", "name", "native_name")
    search_fields = ("name", "native_name")
    list_filter = ("i_recommend", "rating")
    prepopulated_fields = {"slug": ("name",)}

    def poster_preview_tag(self, obj: Product):
        if not obj.poster:
            return ''
        return format_html(
            '<img src="{}" width="45px" height="45px"/>'.format(obj.poster.url)
        )

    poster_preview_tag.allow_tags = True
    poster_preview_tag.short_description = 'Превью'


admin.site.register(Product, CommonAdmin)
