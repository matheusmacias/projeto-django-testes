# Generated by Django 4.2.1 on 2023-05-28 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_category_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category',
            new_name='categories',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]
