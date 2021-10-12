from django.contrib import admin

from .models import Film, Series

class CommonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'native_name', 'rating', 'recomend_to_watch')
    list_display_links = ('id', 'name', 'native_name')
    search_fields = ('name', 'native_name')
    list_filter = ('recomend_to_watch', 'rating')
    prepopulated_fields = {'slug': ('name',)}

class FilmAdmin(CommonAdmin):
    pass


class SeriesAdmin(CommonAdmin):
    pass


admin.site.register(Film, FilmAdmin)
admin.site.register(Series, SeriesAdmin)