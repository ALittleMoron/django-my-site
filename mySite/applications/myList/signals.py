from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from slugify import slugify

# from .models import Product, RatingItem


# @receiver(pre_save, sender=Product)
# def add_slug(sender, instance, *args, **kwargs):
#     """Обычный сигнал для добавления слага перед сохранением

#     Не использую стандартный встроенный в django slugify, потому что он не работает с кириллицей.
#     """
#     instance.slug = slugify(instance.name)
    
    
# @receiver(post_save, sender=Product)
# def rating_post_add(sender, instance, created, **kwargs):
#     """ Сигнал для создания рейтинга для модели Product после её создания. """
#     if created:
#         Rating.objects.get_or_create(parent_product=instance)