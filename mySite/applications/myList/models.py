from itertools import groupby
from operator import attrgetter

from django.core.validators import MaxValueValidator, MinValueValidator 
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

RATING_PURPOSE_TYPES = [
    ('O', 'Беспристрастное мнение'),
    ('P', 'Личное мнение')
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


class Round(models.Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s)'


class ProductQuerySet(models.QuerySet):
    def product_status(self, product_type):
        return self.filter(product_type=product_type).order_by('status')


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def separated_by_status(self, product_type):
        query = self.get_queryset().product_status(product_type)
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
    review_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Число повторных ознакомлений',
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

    def get_vorbosed_product_type(self):
        return list(filter(lambda x: x[0] == self.product_type, PRODUCT_TYPE))[0][1]

    def __str__(self) -> str:
        return f"{self.get_vorbosed_product_type()} \"{self.name}\""
    
    def __repr__(self) -> str:
        return f'{self.get_vorbosed_product_type()} <{self.pk=}, {self.name=}, {self.native_name=}>'

    class Meta:
        verbose_name = "Произведение"
        verbose_name_plural = "Произведения"
        ordering = ["status"]


class Rating(models.Model):
    """ Класс модели рейтинговой системы для тайтлов библиотеки.
    
    Представляет собой расширенную версию, состоящую из множественных оценочных атрибутов тайтла.
    Основная задача - показать разную оценку продукту (чисто ИМХО и псевдо-объективную) и уточнить
    их путем разбиения этих оценок на подоценки (режиссура, сценарий, непротиворечивость - для 
    фильмов/сериалов/аниме и т.д. для остальных продуктов) со своим весом в итоговой оценке.
    """

    parent_product = models.OneToOneField(
        Product,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Произведение'
    )
    positive_offset = models.IntegerField(
        default=0,
        verbose_name='сдвиг оценки',
        validators=[MinValueValidator(0), MaxValueValidator(4)]
    )

    @property
    def avarage_rating_score(self) -> dict[str, float]:
        return RatingItem.objects.filter(parent=self).aggregate(
            o_avg=Round(models.Avg('score', filter=models.Q(rating_purpose_type='O'))),
            p_avg=Round(models.Avg('score', filter=models.Q(rating_purpose_type='P')))
        )
    
    def __str__(self) -> str:
        return f'Рейтинг для "{self.parent_product.name}"'
    
    def __repr__(self) -> str:
        return f'Рейтинг <{self.pk=}, {self.positive_offset=}>'

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class RatingItem(models.Model):
    """ Класс модели элемента рейтинговой системы для тайтлов библиотеки. """
    
    parent = models.ForeignKey(
        Rating,
        related_name='ratingItems',
        verbose_name='Родительский класс',
        on_delete=models.CASCADE,
    )
    label = models.CharField(max_length=100, verbose_name='Пометка')
    rating_purpose_type = models.CharField(
        max_length=1,
        default='O',
        choices=RATING_PURPOSE_TYPES,
        verbose_name='Направленность элемента рейтинга'
    )
    explanation = models.TextField(
        null=True, blank=True, verbose_name='Объяснение',
    )
    score = models.IntegerField(
        default=0, choices=RATING_CHOICES, verbose_name="Оценка",
    )

    def __str__(self) -> str:
        return f'Элемент рейтинга "{self.parent}"'
    
    def __repr__(self) -> str:
        return f'Подрейтинг <{self.pk=}, {self.label=}, {self.score=}>'
    
    class Meta:
        verbose_name = "Элемент рейтинга"
        verbose_name_plural = "Элементы рейтинга"
        ordering = ["-label"]