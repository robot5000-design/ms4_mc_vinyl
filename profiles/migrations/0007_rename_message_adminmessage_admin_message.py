# Generated by Django 3.2.3 on 2021-06-28 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_adminmessage_ordermessage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminmessage',
            old_name='message',
            new_name='admin_message',
        ),
    ]
