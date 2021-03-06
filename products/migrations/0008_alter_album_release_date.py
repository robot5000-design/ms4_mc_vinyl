# Generated by Django 3.2.3 on 2021-05-30 16:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_album_track_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(2021, message='Year in format YYYY'), django.core.validators.MinValueValidator(1900, message='Year in format YYYY')]),
        ),
    ]
