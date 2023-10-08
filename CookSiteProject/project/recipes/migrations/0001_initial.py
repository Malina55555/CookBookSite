# Generated by Django 4.2.6 on 2023-10-08 17:51

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
                ('recipe_name', models.CharField(max_length=255)),
                ('recipe_ingredients', models.CharField(max_length=255)),
                ('recipe_process', models.CharField(max_length=255)),
            ],
        ),
    ]