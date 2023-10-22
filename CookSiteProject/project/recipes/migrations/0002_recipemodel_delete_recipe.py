# Generated by Django 4.2.6 on 2023-10-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.PositiveIntegerField()),
                ('recipe_name', models.CharField(max_length=255)),
                ('recipe_ingredients', models.CharField(max_length=255)),
                ('recipe_process', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]
