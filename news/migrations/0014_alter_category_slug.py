# Generated by Django 5.0.6 on 2025-01-03 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_category_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]