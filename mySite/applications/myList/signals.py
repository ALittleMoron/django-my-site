from django.db.models.signals import pre_save
from django.dispatch import receiver
from slugify import slugify

from .models import Product


@receiver(pre_save, sender=Product)
def add_slug(sender, instance, *args, **kwargs):
    """Обычный сигнал для добавления слага перед сохранением

    Не использую стандартный встроенный в django slugify, потому что он не работает с кириллицей.
    """
    instance.slug = slugify(instance.name)