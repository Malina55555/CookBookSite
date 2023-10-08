from django.test import TestCase

from .models import Recipe

class RecipeTests(TestCase):
    """Recipe model tests"""

    def test_str(self):

        recipe = Recipe(recipe_name='Apple pie',
                      recipe_ingredients='3x Apple, 1x completed pie',
                      recipe_process='cut 3 apples and move them on the pie. You have apple pie!)')
        self.assertEquals(
            str(recipe),
            'Apple pie 3x Apple, 1x completed pie cut 3 apples and move them on the pie. You have apple pie!)'
        )
# Create your tests here.
