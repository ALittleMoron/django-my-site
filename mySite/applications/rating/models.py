from itertools import groupby
from operator import attrgetter

from django.core.validators import MaxValueValidator, MinValueValidator 
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


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


class Round(models.Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s)'


class RatingItemQuerySet(models.QuerySet):
    def separated_by_purpose_type(self):
        query = self.order_by('rating_purpose_type')
        dict_ = {
            k: list(vs)
            for k, vs in groupby(query, attrgetter('rating_purpose_type'))
        }
        return {
            type1: dict_.get(type0, [])
            for type0, type1 in RATING_PURPOSE_TYPES
        }


class RatingItemManager(models.Manager):
    def get_queryset(self):
        return RatingItemQuerySet(self.model, using=self._db)

    def separated_by_purpose_type(self):
        return self.get_queryset().separated_by_purpose_type()


class RatingItem(models.Model):
    """ Класс модели элемента рейтинговой системы для тайтлов библиотеки. """
    
    objects = RatingItemManager()
    label = models.CharField(max_length=100, verbose_name='Пометка')
    positive_offset = models.IntegerField(
        default=0,
        verbose_name='сдвиг оценки',
        validators=[MinValueValidator(0), MaxValueValidator(4)]
    )
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
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # FIXME: переделать под особенности ContentType
    # @property
    # def avarage_rating_score(self) -> dict[str, float]:
    #     return RatingItem.objects.filter(parent=self).aggregate(
    #         o_avg=Round(models.Avg('score', filter=models.Q(rating_purpose_type='O'))),
    #         p_avg=Round(models.Avg('score', filter=models.Q(rating_purpose_type='P')))
    #     )


    def __str__(self) -> str:
        return f'рейтинг для "{self.content_object if self.content_object else "пусоты"}"'
    
    def __repr__(self) -> str:
        return f'RatingItem({self.pk=}, {self.label=}, {self.score=})'
    
    class Meta:
        verbose_name = "Элемент рейтинга"
        verbose_name_plural = "Элементы рейтинга"
        ordering = ["-label"]