from django.contrib import admin

from .models import GitHubRepositoryCard


class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "repo_name", "repo_avg_lang", "repo_licence", "is_published")
    list_filter = ("repo_avg_lang", "is_published", "repo_licence")


admin.site.register(GitHubRepositoryCard, CardAdmin)
