# Generated by Django 4.2.2 on 2023-06-21 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='description',
            new_name='descrtion',
        ),
    ]
