# Generated by Django 4.0.6 on 2022-07-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_project_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='portfolio/images/'),
        ),
    ]
