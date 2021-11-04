from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse
from slugify import slugify


class Product(models.Model):
    RATING_CHOICES = [
        (0, "Не указан"),
        (1, "Хуже некуда"),
        (2, "Ужасно"),
        (3, "Очень плохо"),
        (4, "Плохо"),
        (5, "Более-менее"),
        (6, "Нормально"),
        (7, "Хорошо"),
        (8, "Очень хорошо"),
        (9, "Великолепно"),
        (10, "Шедевр"),
    ]
    PRODUCT_TYPE = [
        ("film", "Фильм"),
        ("series", "Сериал"),
        ("anime", "Аниме"),
        ("game", "Игра"),
        ("book", "Книга"),
    ]

    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    native_name = models.CharField(
        max_length=150, unique=True, verbose_name="Название на родном языке"
    )
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    opinion = models.TextField(null=True, blank=True, verbose_name="Мое мнение")
    slug = models.SlugField(max_length=160, null=True, verbose_name="Слаг")
    rating = models.IntegerField(
        default=0, choices=RATING_CHOICES, verbose_name="Оценка"
    )
    i_recommend = models.BooleanField(
        default=False, verbose_name="Рекомендую к ознакомлению"
    )
    url = models.URLField(null=True, blank=True, verbose_name="Ссылка на ознакомление")
    poster = models.ImageField(
        blank=True, null=True, upload_to="posters/%Y/%m/%d", verbose_name="Постер"
    )
    product_type = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        choices=PRODUCT_TYPE,
        verbose_name="Тип произведения",
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def get_absolute_url(self) -> str:
        return reverse("myList/productDetail", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return f"Тайтл <{self.name} - {self.product_type}>"

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"
        ordering = ["-rating"]


@receiver(pre_save, sender=Product)
def add_slug(sender, instance, *args, **kwargs):
    """Обычный сигнал для добавления слага перед сохранением

    Не использую стандартный встроенный в django slugify, потому что он не работает с кириллицей.
    """
    instance.slug = slugify(instance.name)
