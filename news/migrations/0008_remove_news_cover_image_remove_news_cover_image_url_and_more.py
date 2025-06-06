# Generated by Django 5.0.6 on 2024-11-22 07:34

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_news_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='cover_image',
        ),
        migrations.RemoveField(
            model_name='news',
            name='cover_image_url',
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_images')),
                ('umage_url', models.CharField(blank=True, max_length=200, null=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='news.news')),
            ],
        ),
    ]
