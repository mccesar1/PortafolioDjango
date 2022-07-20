# Generated by Django 4.0.6 on 2022-07-19 17:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='blog/images/')),
                ('date', models.DateTimeField(verbose_name=datetime.date.today)),
            ],
            options={
                'verbose_name_plural': 'posts',
            },
        ),
    ]
