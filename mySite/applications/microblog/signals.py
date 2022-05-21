from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from slugify import slugify

from .models import Post


@receiver(pre_save, sender=Post)
def presave_fields(sender, instance, *args, **kwargs):
    """Обычный сигнал для изменения времени публикации и добавление слага."""
    if instance.is_published and instance.published_at is None:
        instance.published_at = timezone.now()
    elif not instance.is_published and instance.published_at is not None:
        instance.published_at = None

    instance.slug = slugify(instance.title)
