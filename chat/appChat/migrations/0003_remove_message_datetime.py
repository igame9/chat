# Generated by Django 4.1.2 on 2022-10-06 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appChat', '0002_rename_дата и время_message_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='dateTime',
        ),
    ]
