# Generated by Django 3.1.7 on 2021-03-13 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='review',
        ),
    ]
