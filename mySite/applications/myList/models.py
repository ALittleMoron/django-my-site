from itertools import groupby
from operator import attrgetter

from django.db import models
from django.urls import reverse


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

PRODUCT_STATUS = [
    ('pn', 'Запланировано'),
    ('ga', 'В процессе (Ознакомляюсь)'),
    ('rv', 'Повтор'),
    ('ac', 'Завершено'),
    ('ab', 'Брошено'),
    ('pp', 'Отложено'),
]


class ExtendedManager(models.Manager):
    def separated_by_status(self, product_type):
        query = super().get_queryset().filter(product_type=product_type).order_by('status')
        dict_ = {
            k: list(vs)
            for k, vs in groupby(query, attrgetter('status'))
        }
        return {
            status1: dict_.get(status0, [])
            for status0, status1 in PRODUCT_STATUS
        }


class Product(models.Model):
    objects = ExtendedManager()
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    native_name = models.CharField(
        max_length=150, unique=True, verbose_name="Название на родном языке"
    )
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    opinion = models.TextField(null=True, blank=True, verbose_name="Мое мнение")
    slug = models.SlugField(max_length=160, null=True, verbose_name="Слаг")
    status = models.CharField(
        max_length=3,
        blank=False,
        null=False,
        choices=PRODUCT_STATUS,
        default='ac',
        verbose_name='Статус',
    )
    review_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Число повторных ознакомлений',
    )
    rating = models.IntegerField(
        default=0, choices=RATING_CHOICES, verbose_name="Оценка"
    )
    i_recommend = models.BooleanField(
        default=False, verbose_name="Рекомендую"
    )
    url = models.URLField(null=True, blank=True, verbose_name="Ссылка")
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
