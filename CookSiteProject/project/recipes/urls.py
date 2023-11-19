from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view()), #{}
    path('allrecipes', views.AllRecipesView.as_view()), # {'get_recipes': array} <- {'id': id, 'name': name, 'type': type, 'ingredients': ingredients, 'process': process}

    path('user-info/<int:id>', views.UserInfoView.as_view()), # {'is_exist': 'true', 'id': id, 'name': name, 'email': email, 'password': '***'}
    path('recipe-info/<int:r_id>', views.RecipeInfoView.as_view()), #в определнный момент перестало работать # {'is_exist': 'true', 'id': id, 'name': name, 'type': type, 'ingredients': ingredients, 'process': process}
    path('recipe-info/<str:name>', views.RecipeInfoView.as_view()), # {'is_exist': 'true', 'get_recipes': array} <- {'id': id, 'name': name, 'type': type, 'ingredients': ingredients, 'process': process}

    path('create-user', views.CreateNewUser.as_view()),  #необходимо протестировать с помощью фронта

    path('create-comment/<int:id_recipe>/<content>/<int:id_writer>', views.CreateNewComment.as_view()), # {'comment-status': 'saved'} or {'comment-status': 'smth or smbd is not existing'}
]