# Generated by Django 5.0.6 on 2024-06-23 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='phone',
            new_name='phonenumber',
        ),
    ]
