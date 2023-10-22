from django.db import models

# Create your models here.

class RecipeModel(models.Model):

    recipe_id = models.PositiveIntegerField()
    recipe_name = models.CharField( max_length=255, )
    recipe_ingredients = models.CharField( max_length=255, )
    recipe_process = models.CharField( max_length=255, )

    def __str__(self):
        return ' '.join([
            str(self.recipe_id),
            self.recipe_name,
            self.recipe_ingredients,
            self.recipe_process,
        ])

class UserModel(models.Model):

    user_id = models.PositiveIntegerField()
    user_name = models.CharField( max_length=255, )
    user_email = models.CharField(max_length=255, )
    user_password = models.CharField(max_length=255, )

    def __str__(self):
        return ' '.join([
            str(self.user_id),
            self.user_name,
            self.user_email,
            self.user_password,
        ])

class SaveModel(models.Model):

    save_saver_id = models.PositiveIntegerField()
    save_recipe_id = models.PositiveIntegerField()