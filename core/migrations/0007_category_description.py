# Generated by Django 4.2.1 on 2023-05-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_categories_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]