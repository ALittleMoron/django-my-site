from typing import Any
from django.contrib import admin

from .models import GitHubRepositoryCard


class CardAdmin(admin.ModelAdmin):
    list_filter = ('repo_avg_lang', 'is_published')
    

admin.site.register(GitHubRepositoryCard, CardAdmin)