# Generated by Django 5.0.6 on 2024-08-06 17:38

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField(verbose_name='target date')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='date created')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='date updated')),
                ('description', models.TextField(max_length=300)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='news_cover')),
                ('cover_image_url', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
