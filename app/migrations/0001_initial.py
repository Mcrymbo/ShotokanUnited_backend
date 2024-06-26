# Generated by Django 5.0.6 on 2024-06-18 19:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('venue', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('poster_image', models.ImageField(blank=True, null=True, upload_to='images/poster_images/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
