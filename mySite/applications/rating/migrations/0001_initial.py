# Generated by Django 3.2.7 on 2022-01-31 16:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, verbose_name='Пометка')),
                ('positive_offset', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)], verbose_name='сдвиг оценки')),
                ('rating_purpose_type', models.CharField(choices=[('O', 'Беспристрастное мнение'), ('P', 'Личное мнение')], default='O', max_length=1, verbose_name='Направленность элемента рейтинга')),
                ('explanation', models.TextField(blank=True, null=True, verbose_name='Объяснение')),
                ('score', models.IntegerField(choices=[(0, 'Не указан'), (1, 'Хуже некуда'), (2, 'Ужасно'), (3, 'Очень плохо'), (4, 'Плохо'), (5, 'Более-менее'), (6, 'Нормально'), (7, 'Хорошо'), (8, 'Очень хорошо'), (9, 'Великолепно'), (10, 'Шедевр')], default=0, verbose_name='Оценка')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Элемент рейтинга',
                'verbose_name_plural': 'Элементы рейтинга',
                'ordering': ['-label'],
            },
        ),
    ]
