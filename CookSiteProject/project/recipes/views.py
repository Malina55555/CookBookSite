from django.shortcuts import render, redirect #?
from django.views.generic import ListView #?
from django.http import HttpResponse #?
from django.db.models import Max
from django.contrib.auth import authenticate, login, logout #?
from django.contrib import messages #?
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


class MainView(APIView): #YES
    def get (self, request):
        return Response({})


class AllRecipesView(APIView): #YES
    def get (self, request):
        get_recipes = RecipeModel.objects.all()
        array = []
        for recipe in get_recipes:
            id = recipe.recipe_id
            name = recipe.recipe_name
            ingredients = recipe.recipe_ingredients
            process = recipe.recipe_process
            type = recipe.recipe_type
            line = {'id': id, 'name': name, 'type': type, 'ingredients': ingredients, 'process': process}
            array.append(line)
        return Response({'get_recipes': array})


class RecipeInfoView(APIView):
    def get(self, request, r_id): #перестало работать
        if RecipeModel.objects.filter(recipe_id=r_id).exists():
            #get_recipe = RecipeModel.objects.get(recipe_id=id)
            #id = get_recipe.recipe_id
            #name = get_recipe.recipe_name
            #ingredients = get_recipe.recipe_ingredients
           # process = get_recipe.recipe_process
          #  type = get_recipe.recipe_type
         #   return Response({'is_exist': 'true', 'id': id, 'name': name, 'type': type, 'ingredients': ingredients, 'process': process})
        #else:
            return Response({'is_exist': 'true', 'id': id, 'name': '', 'type': '', 'ingredients': '', 'process': ''})

    def get (self, request, name): #YES
        array = []
        if RecipeModel.objects.filter(recipe_name=name).exists():
            get_recipes = RecipeModel.objects.filter(recipe_name=name)
            for recipe in get_recipes:
                id = recipe.recipe_id
                name = recipe.recipe_name
                ingredients = recipe.recipe_ingredients
                process = recipe.recipe_process
                type = recipe.recipe_type
                line = {'id': id, 'name': name, 'type': type, 'ingredients': ingredients, 'process': process}
                array.append(line)
            return Response({'is_exist-name': 'true', 'get_recipes': array})
        else:
            return Response({'is_exist-name': 'false', 'get_recipes': []})





# Далее views, связанные с аккаунтами


class UserInfoView(APIView): #YES
    def get(self, request, id):
        if UserModel.objects.filter(user_id=id).exists():
            get_acc = UserModel.objects.get(user_id=id)
            name = get_acc.user_name
            email = get_acc.user_email
            return Response({'is_exist': 'true', 'id': id, 'name': name, 'email': email, 'password': '***'})
        else:
            return Response({'is_exist': 'false', 'id': id, 'name': '', 'email': '', 'password': ''})


class CreateNewComment(APIView):
    def get(self, request, id_recipe, content, id_writer):
        if UserModel.objects.filter(user_id=id_writer).exists() and RecipeModel.objects.filter(recipe_id=id_recipe).exists():
            #try:
                CommentModel.objects.create(comment_recipe_id=id_recipe, comment_content=content, comment_writer_id=id_writer)
                return Response({'comment-status': 'saved'})
            #except:
             #   return Response({'comment-status': 'smth goes wrong'})
        else:
            return Response({'comment-status': 'smth or smbd is not existing'})




#надо проверять с кнопками, а так не факт, что работает


class CreateNewUser(APIView):
    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if UserModel.objects.filter(user_email=email).exists():
            return Response({'user_status': 'user with this email is already exists'})
        else:
            new_id = UserModel.objects.get(user_id=Max('user_id')) + 1
            UserModel.objects.create(user_id=new_id, user_name=name, user_email=email, user_password=password)
            return Response({'user_status': 'was created'})


class SignInView(APIView):
    def post (self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            password = request.POST.get('password')
            user = authenticate(request, name=name, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
            else:
                return Response({'signin_status': 'Имя пользователя или пароль введены неправильно. Если у вас нет аккаунта - зарегистрируйтесь.'})
                #messages.info(request, 'Имя пользователя или пароль введены неправильно. Если у вас нет аккаунта - зарегистрируйтесь.') # Возможно нужно заменить на место в html под ошибки?

"""
class SignInView(APIView):
    def post (self, request):
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, name=name, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
        else:
            messages.info(request, 'Имя пользователя или пароль введены неправильно. Если у вас нет аккаунта - зарегистрируйтесь.') # Возможно нужно заменить на место в html под ошибки?

class RegistaratoinView(APIView): 
    def get (self, request):
        return render(request, "reg.html", {})
    def post (self, request):
        new_id = UserModel.objects.get(user_id=Max('user_id')) + 1
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        UserModel.objects.create(user_id=new_id, user_name=name, user_email=email, user_password=password)
        return render(request, 'signIn.html', {'name': name})

def logout_user(request): #no need
    logout(request)
    return redirect('home')
"""
