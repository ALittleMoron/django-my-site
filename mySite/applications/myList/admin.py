from django.contrib import admin

from .models import Product

class CommonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'native_name', 'rating', 'i_recommend')
    list_display_links = ('id', 'name', 'native_name')
    search_fields = ('name', 'native_name')
    list_filter = ('i_recommend', 'rating')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, CommonAdmin)