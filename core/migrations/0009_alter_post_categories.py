# Generated by Django 4.2.1 on 2023-05-28 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_category_post_categories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='core.category'),
        ),
    ]
