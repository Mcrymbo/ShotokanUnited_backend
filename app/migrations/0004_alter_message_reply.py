# Generated by Django 5.0.6 on 2024-07-02 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_message_reply_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='reply',
            field=models.TextField(blank=True, max_length=400, null=True),
        ),
    ]
