from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class GitHubRepositoryCard(models.Model):
    """Класс модели карточки ГитХаб репозитория."""

    repo_url = models.URLField(verbose_name="URL репозитория", max_length=200)
    repo_name = models.CharField(
        verbose_name="Название проекта", max_length=100, default="no name"
    )
    repo_avg_lang = models.CharField(
        verbose_name="Язык программирования(с бо́льшим процентом кода)",
        max_length=20,
        default="no language",
    )
    repo_description = models.CharField(
        verbose_name="Описание репозитория", max_length=200, null=True, blank=True
    )
    repo_licence = models.CharField(
        verbose_name="Лицензия репозитория", max_length=200, null=True, blank=True
    )
    is_published = models.BooleanField(verbose_name="Опубликовано?", default=False)

    class Meta:
        verbose_name = "Карточка GitHub"
        verbose_name_plural = "Карточки GitHub"

    def __str__(self):
        return self.repo_name

    def get_absolute_url(self):
        return self.repo_url
