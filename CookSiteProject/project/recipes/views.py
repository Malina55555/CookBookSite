from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


""" View, выдающий ничего """


class MainView(APIView):
    def get(self, request):
        return Response({})


""" Views, связанные с выборкой рецептов """


class CreateNewRecipe(APIView):
    def post(self, request):
        name = request.data.get('name')
        ingredients = request.data.get('ingredients')
        process = request.data.get('process')
        type = request.data.get('type')
        #image = request.data.get('image')
        new_id = RecipeModel.objects.all().order_by("-id")[0].id
        new_id += 1
        try:
            RecipeModel.objects.create(id = new_id, recipe_id=new_id, recipe_name=name, recipe_ingredients=ingredients,
                                       recipe_process=process, recipe_type=type) #,recipe_image=image )
            return Response({'recipe_status': 'was created'})
        except:
            return Response({'recipe_status': 'smth is wrong'})


class AllRecipesView(APIView):
    def get(self, request):
        get_recipes = RecipeModel.objects.all()
        array = []
        for recipe in get_recipes:
            id = recipe.recipe_id
            name = recipe.recipe_name
            ingredients = recipe.recipe_ingredients
            process = recipe.recipe_process
            type = recipe.recipe_type
            image = recipe.recipe_image
            line = {'id': id, 'name': name, 'type': type, 'ingredients': ingredients, 'process': process, 'image': image}
            array.append(line)
        return Response({'get_recipes': array})


class RecipeInfoView(APIView):
    def get(self, request, r_id):
        if RecipeModel.objects.filter(recipe_id=r_id).exists():
            get_recipe = RecipeModel.objects.get(recipe_id=r_id)
            id = get_recipe.recipe_id
            name = get_recipe.recipe_name
            ingredients = get_recipe.recipe_ingredients
            process = get_recipe.recipe_process
            type = get_recipe.recipe_type
            image = get_recipe.recipe_image
            return Response({'is_exist': 'true', 'id': id, 'name': name, 'type': type, 'ingredients': ingredients, 'process': process, 'image': image})
        else:
            return Response({'is_exist': 'true', 'id': r_id, 'name': '', 'type': '', 'ingredients': '', 'process': '', 'image': ''})


class TypeRecipesView(APIView):
    def post (self, request):
        type = request.data.get("type")
        get_recipes = RecipeModel.objects.filter(recipe_type=type).order_by("id")
        array = []
        for recipe in get_recipes:
            id = recipe.recipe_id
            name = recipe.recipe_name
            ingredients = recipe.recipe_ingredients
            process = recipe.recipe_process
            type = recipe.recipe_type
            image = recipe.recipe_image
            line = {'id': id, 'name': name, 'type': type, 'ingredients': ingredients, 'process': process, 'image': image}
            array.append(line)
        return Response({'get_recipes': array})


""" Views, связанные с выборкой пользователей """


class CreateNewUser(APIView):
    def post(self, request):
        print(request.POST)
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        if UserModel.objects.filter(user_email=email).exists():
            return Response({'user_status': 'user with this email is already exists'})
        else:
            new_id = UserModel.objects.all().order_by("-id")[0].id
            new_id += 1
            UserModel.objects.create(id=new_id, user_id=new_id, user_name=name, user_email=email, user_password=password)
            return Response({'user_status': 'was created'})


class UserInfoView(APIView):
    def get(self, request, id):
        if UserModel.objects.filter(user_id=id).exists():
            get_acc = UserModel.objects.get(user_id=id)
            name = get_acc.user_name
            email = get_acc.user_email
            return Response({'is_exist': 'true', 'id': id, 'name': name, 'email': email, 'password': '***'})
        else:
            return Response({'is_exist': 'false', 'id': id, 'name': '', 'email': '', 'password': ''})


class SignInView(APIView):
    def post (self, request):
            email = request.data.get('email')
            password = request.data.get('password')
            try:
                user = UserModel.objects.get(user_email=email)
                if password == user.user_password:
                    return Response({'signin_status': 'ok', 'user_id': user.user_id})
                else:
                    return Response({'signin_status': 'password is wrong'})
            except UserModel.DoesNotExist:
                return Response({'signin_status': 'user doesnot exist'})


""" Views, связанные с выборкой комментариев """


class CreateNewComment(APIView):
    def post (self, request):
        id_writer = request.data.get('id_writer')
        id_recipe = request.data.get('id_recipe')
        content = request.data.get('content')
        if UserModel.objects.filter(user_id=id_writer).exists() and RecipeModel.objects.filter(recipe_id=id_recipe).exists():
                CommentModel.objects.create(comment_recipe_id=id_recipe, comment_content=content, comment_writer_id=id_writer)
                return Response({'comment-status': 'saved'})
        else:
            return Response({'comment-status': 'smth or smbd is not existing'})


class CommentsOfRecipe(APIView):
    def get(self, request, id):
        if CommentModel.objects.filter(comment_recipe_id=id).exists():
            comments = CommentModel.objects.filter(comment_recipe_id=id)
            array = []
            for com in comments:
                content = com.comment_content
                name = UserInfoView.get(self, request, com.comment_writer_id).data['name']
                line = {'name': name, 'content': content}
                array.append(line)
            return Response({'recipe is exist': 'true', 'get_comments': array})
        else:
            return Response({'recipe is exist': 'false', 'get_comments': ''})


""" Views, связанные с выборкой из таблицы связей Избранное """


class CreateNewSave(APIView):
    def get(self, request, save_saver_id, save_recipe_id):
        if UserModel.objects.filter(user_id=save_saver_id).exists() and RecipeModel.objects.filter(recipe_id=save_recipe_id).exists():
                SaveModel.objects.create(save_saver_id=save_saver_id, save_recipe_id=save_recipe_id)
                return Response({'save-status': 'saved'})
        else:
            return Response({'save-status': 'smth or smbd is not existing'})


class SavedRecipes(APIView):
    def get(self, request, id):
        if UserModel.objects.filter(user_id=id).exists():
            saved_id = SaveModel.objects.filter(save_saver_id=id)
            array = []
            for save in saved_id:
                r_id = save.save_recipe_id
                recipe = RecipeInfoView.get(self, request, r_id).data
                name = recipe['name']
                ingredients = recipe['ingredients']
                process = recipe['process']
                type = recipe['type']
                image = recipe['image']
                line = {'id': r_id, 'name': name, 'type': type, 'ingredients': ingredients, 'process': process, 'image': image}
                array.append(line)
            return Response({'saver is exist':'true', 'get_recipes': array})
        else:
            return Response({'saver is exist':'false', 'get_recipes': '[]'})
