# Generated by Django 5.0.6 on 2024-11-02 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_notification_message_remove_notification_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, default='', unique=True),
        ),
    ]
