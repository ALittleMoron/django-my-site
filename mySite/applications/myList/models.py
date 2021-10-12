from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from slugify import slugify


class CommonInfo(models.Model):
    RatingChoices = [
        (0, 'Не указан'),
        (1, 'Хуже некуда'),
        (2, 'Ужасно'),
        (3, 'Очень плохо'),
        (4, 'Плохо'),
        (5, 'Более-менее'),
        (6, 'Нормально'),
        (7, 'Хорошо'),
        (8, 'Очень хорошо'),
        (9, 'Великолепно'),
        (10, 'Шедевр'),
    ]
    
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    native_name = models.CharField(max_length=150, unique=True, verbose_name='Название на родном языке')
    description = models.TextField(verbose_name='Описание')
    opinion = models.TextField(verbose_name="Мое мнение")
    slug = models.SlugField(max_length=160, null=True, verbose_name='Слаг')
    rating = models.IntegerField(default=0, choices=RatingChoices, verbose_name='Оценка')
    recomend_to_watch = models.BooleanField(default=False, verbose_name='Рекомендую к ознакомлению')
    url = models.URLField(null=True, blank=True, verbose_name='Ссылка на ознакомление')
    
    class Meta:
        abstract = True


class Film(CommonInfo):
    is_anime = models.BooleanField(default=False, verbose_name='Аниме')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['rating']


class Series(CommonInfo):
    is_anime = models.BooleanField(default=False, verbose_name='Аниме')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Сериал"
        verbose_name_plural = "Сериалы"
        ordering = ['rating']


# class VideoGame(CommonInfo):
#     pass


@receiver(pre_save, sender=Film)
@receiver(pre_save, sender=Series)
def add_slug(sender, instance, *args, **kwargs):
    """ Обычный сигнал для добавления слага перед сохранением
    
    Не использую стандартный встроенный в django slugify, потому что он не работает с кириллицей.
    """
    instance.slug = slugify(instance.name)
    