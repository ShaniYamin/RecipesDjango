# Generated by Django 4.2.7 on 2023-12-11 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=300)),
                ('author_name', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('prep_time', models.IntegerField()),
                ('cook_time', models.IntegerField()),
                ('total_time', models.IntegerField()),
                ('servings', models.IntegerField()),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('tips', models.TextField()),
            ],
        ),
    ]
