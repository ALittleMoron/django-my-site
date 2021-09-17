from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from django.forms import widgets

from .models import Post


class CKPostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'text': CKEditorUploadingWidget
        }


class PostAdmin(admin.ModelAdmin):
    form = CKPostAdminForm
    
    list_display = ('id', 'title', 'created_at', 'updated_at', 'published_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'tags')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'tags')
    prepopulated_fields = {'slug': ('title',)} 


admin.site.register(Post, PostAdmin)