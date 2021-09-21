from django.db import models
from django.urls import reverse
from django.utils import timezone
from slugify import slugify
from taggit.managers import TaggableManager


class Post(models.Model):
    """ Класс модели постов моего микроблога.
    
    Автора нет, так как им в 100% случаев буду только я.
    """
    title = models.CharField(max_length=255, unique=True, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    slug = models.SlugField(null=True, max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата написания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    published_at = models.DateTimeField(blank=True, null=True, verbose_name="Дата публикации")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано?")
    tags = TaggableManager()
    
    def save(self, *args, **kwargs):
        if self.is_published and self.published_at is None:
            self.published_at = timezone.now()
        elif not self.is_published and self.published_at is not None:
            self.published_at = None

        if not self.slug:
            self.slug = slugify(self.title)
        
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("microblog/postDetail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ['updated_at']
