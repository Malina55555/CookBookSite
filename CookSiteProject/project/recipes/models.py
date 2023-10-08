from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(
        max_length=255,
    )
    recipe_ingredients = models.CharField(
        max_length=255,
    )
    recipe_process = models.CharField(
        max_length=255,
    )
    #email = models.EmailField()

    def __str__(self):
        return ' '.join([
            self.recipe_name,
            self.recipe_ingredients,
            self.recipe_process
        ])