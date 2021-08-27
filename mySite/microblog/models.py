from taggit.managers import TaggableManager
from django.db import models

# Create your models here.


class Post(models.Model):
    """ Класс модели постов моего микроблога.
    
    Автора нет, так как им в 100% случаев буду только я.
    """
    title = models.CharField(max_length=255, unique=True, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата написания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    published_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано?")
    tags = TaggableManager()
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['updated_at']