from django.db import models


class RecipeModel(models.Model):
    recipe_id = models.PositiveIntegerField()
    recipe_name = models.CharField( max_length=255)
    recipe_ingredients = models.CharField( max_length=255)
    recipe_process = models.CharField( max_length=2500)
    recipe_type = models.CharField(max_length=15)
    recipe_image = models.CharField(max_length=255)


class UserModel(models.Model):
    user_id = models.PositiveIntegerField()
    user_name = models.CharField( max_length=255)
    user_email = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)


class SaveModel(models.Model):
    save_saver_id = models.PositiveIntegerField()
    save_recipe_id = models.PositiveIntegerField()


class CommentModel(models.Model):
    comment_recipe_id = models.PositiveIntegerField()
    comment_content = models.CharField(max_length=1000)
    comment_writer_id = models.PositiveIntegerField()