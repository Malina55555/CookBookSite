from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view()),

    path('create-recipe', views.CreateNewRecipe.as_view()),
    path('allrecipes', views.AllRecipesView.as_view()),
    path('recipe-info/<int:r_id>', views.RecipeInfoView.as_view()),
    path('recipe-type', views.TypeRecipesView.as_view()),

    path('create-user', views.CreateNewUser.as_view()),
    path('user-info/<int:id>', views.UserInfoView.as_view()),
    path('sign-in', views.SignInView.as_view()),

    path('create-save/<int:save_saver_id>/<int:save_recipe_id>', views.CreateNewSave.as_view()),
    path('saved-users-recipes/<int:id>', views.SavedRecipes.as_view()),

    path('create-comment', views.CreateNewComment.as_view()),
    path('comments/<int:id>', views.CommentsOfRecipe.as_view()),
]