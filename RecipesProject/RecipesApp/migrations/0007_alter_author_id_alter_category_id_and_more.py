# Generated by Django 4.2.7 on 2023-12-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RecipesApp', '0006_category_ingredient_tags_remove_author_age_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='quantity',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tags',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
