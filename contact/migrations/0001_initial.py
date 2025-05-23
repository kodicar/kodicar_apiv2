# Generated by Django 3.1.7 on 2021-03-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField(max_length=3000)),
                ('date_sent', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
