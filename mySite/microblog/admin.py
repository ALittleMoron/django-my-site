from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'published_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'tags')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'tags')


admin.site.register(Post, PostAdmin)