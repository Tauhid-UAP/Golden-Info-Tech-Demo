# Generated by Django 2.2 on 2020-11-29 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='member_id',
        ),
    ]
