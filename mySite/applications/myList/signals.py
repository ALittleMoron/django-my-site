from django.db.models.signals import pre_save
from django.dispatch import receiver
from slugify import slugify

from .models import Anime, Book, Film, Game, Series


@receiver(pre_save, sender=Anime)
@receiver(pre_save, sender=Book)
@receiver(pre_save, sender=Film)
@receiver(pre_save, sender=Game)
@receiver(pre_save, sender=Series)
def add_slug(sender, instance, *args, **kwargs):
    """Обычный сигнал для добавления слага перед сохранением

    Не использую стандартный встроенный в django slugify, потому что он не работает с кириллицей.
    """
    instance.slug = slugify(instance.name)
