# Generated by Django 5.0.6 on 2024-08-23 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_message_options_message_notification_sent_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='message',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
