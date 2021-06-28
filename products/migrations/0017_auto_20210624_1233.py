# Generated by Django 3.2.3 on 2021-06-24 12:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0016_auto_20210621_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productreview',
            name='upvote_list',
        ),
        migrations.AddField(
            model_name='productreview',
            name='upvote_list',
            field=models.ManyToManyField(blank=True, related_name='upvote_users', to=settings.AUTH_USER_MODEL),
        ),
    ]