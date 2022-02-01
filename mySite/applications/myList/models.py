from itertools import groupby
from operator import attrgetter

from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.urls import reverse

from rating.models import RatingItem


PRODUCT_TYPE = [
    ("film", "Фильм"),
    ("series", "Сериал"),
    ("anime", "Аниме"),
    ("game", "Игра"),
    ("book", "Книга"),
]

PRODUCT_STATUS = [
    ('pn', 'Запланировано'),
    ('ga', 'В процессе'),
    ('rv', 'Повтор'),
    ('ac', 'Завершено'),
    ('ab', 'Брошено'),
    ('pp', 'Отложено'),
]


class ProductManager(models.Manager):
    def separated_by_status(self):
        query = self.get_queryset().order_by('status')
        dict_ = {
            k: list(vs)
            for k, vs in groupby(query, attrgetter('status'))
        }
        return {
            status1: dict_.get(status0, [])
            for status0, status1 in PRODUCT_STATUS
        }


class Product(models.Model):
    objects = ProductManager()
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
    i_recommend = models.BooleanField(
        default=False, verbose_name="Рекомендую"
    )
    url = models.URLField(null=True, blank=True, verbose_name="Ссылка")
    poster = models.ImageField(
        blank=True, null=True, upload_to="posters/%Y/%m/%d", verbose_name="Постер"
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    def __str__(self, class_name_verbose, name) -> str:
        return f'{class_name_verbose} "{name}"'

    def __repr__(self, class_name, pk, name, status) -> str:
        return f'{class_name}({pk=}, {name=}, {status=})'

    def get_absolute_url(self):
        return reverse(
            "myList/productDetail",
            kwargs={"model_name": self.__class__.__name__.lower(), "slug": self.slug})
    

    class Meta:
        abstract = True


class Film(Product):
    rating = GenericRelation(RatingItem, related_query_name='films')
    review_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Число повторных просмотров',
    )

    def __str__(self) -> str:
        return super().__str__('Фильм', self.name)

    def __repr__(self) -> str:
        return super().__repr__('Film', self.pk, self.name, self.status)

    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['status']


class Series(Product):
    rating = GenericRelation(RatingItem, related_query_name='series')
    review_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Число повторных просмотров',
    )

    def __str__(self) -> str:
        return super().__str__('Сериал' ,self.name)

    def __repr__(self) -> str:
        return super().__repr__('Series', self.pk, self.name, self.status)

    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'
        ordering = ['status']


class Book(Product):
    rating = GenericRelation(RatingItem, related_query_name='books')
    ISBN = models.CharField(max_length=30, unique=True, verbose_name='Номер книги')

    def __str__(self) -> str:
        return super().__str__('Книга', self.name)

    def __repr__(self) -> str:
        return super().__repr__('Book', self.pk, self.name, self.status)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['status']


class Anime(Product):
    rating = GenericRelation(RatingItem, related_query_name='anime')
    ANIME_TYPE = [
        ('Ov', 'OVA'),
        ('Fi', 'Фильм'),
        ('Se', 'Сериал'),
        ('On', 'ONA'),
        ('Sp', 'Спешл'),
    ]
    
    anime_type = models.CharField(
        max_length=2,
        default='Se',
        choices=ANIME_TYPE,
        verbose_name='Тип аниме'
    )

    def __str__(self) -> str:
        return super().__str__('Аниме', self.name)

    def __repr__(self) -> str:
        return super().__repr__('Anime', self.pk, self.name, self.status)

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'
        ordering = ['status']


class Game(Product):
    rating = GenericRelation(RatingItem, related_query_name='games')

    def __str__(self) -> str:
        return super().__str__('Игра', self.name)

    def __repr__(self) -> str:
        return super().__repr__('Game', self.pk, self.name, self.status)
    
    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['status']