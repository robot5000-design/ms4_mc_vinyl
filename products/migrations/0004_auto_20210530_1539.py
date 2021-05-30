# Generated by Django 3.2.3 on 2021-05-30 15:39

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210530_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='release_date',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(2021, message='Year in format YYYY'), django.core.validators.MinValueValidator(1900, message='Year in format YYYY')]),
        ),
        migrations.AlterField(
            model_name='album',
            name='track_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=50, null=True), default=list, size=None),
        ),
    ]
