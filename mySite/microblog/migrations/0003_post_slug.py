# Generated by Django 3.2.6 on 2021-08-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0002_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=300, null=True, unique=True),
        ),
    ]
