# Generated by Django 4.1.3 on 2022-12-19 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_videouploader_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='videoUploader',
        ),
    ]
