from django.shortcuts import render, redirect #?
from django.views.generic import ListView #?
from django.http import HttpResponse #?
from django.db.models import Max
from rest_framework.response import Response
from rest_framework.views import APIView

class InfoView(APIView): #test will be deleted
    def get (self, request):
        return Response({'name': 'John', 'surname': 'Jackson', 'age': 21})

from .models import RecipeModel

class RecipesInfoView(APIView): #test will be deleted
    def get (self, request):
        get_recipes = RecipeModel.objects.all()
        # return Response({'get_recipes': get_recipes}) # may be this way, but backend worker doesnot how to change .js for this.
        return render(request, 'norecipe.html', {'get_recipes': get_recipes})

class MainView(APIView): #В теории html через js должен фильтровать то, какие рецепты будут показаны.
    def get (self, request):
        get_all_recipes = RecipeModel.objects.all()
        return render(request, 'main.html', {'all_recipes': get_all_recipes})

class NavigationView(APIView):
    def get (self, request):
        return render(request, 'navigation.html', {})


# Далее views, связанные с аккаунтами

from django.contrib.auth import authenticate, login, logout #?
from django.contrib import messages #?
from .models import UserModel

class UserInfoView(APIView): #now working only for anton because .js(
    def get (self, request):
        get_anton = UserModel.objects.get(user_id=1) # dont use filter!!!
        name = get_anton.user_name
        email = get_anton.user_email
        return Response({'name': name, 'email': email, 'password': '***'})

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

class RegistaratoinView(APIView): # ПО НЕИЗВЕСТНОЙ БЭКЕНДЕРУ ПРИЧИНЕ НЕ РАБОТАЕТ
    def get (self, request):
        return render(request, "reg.html", {})
    def post (self, request):
        new_id = UserModel.objects.get(user_id=Max('user_id')) + 1
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        UserModel.objects.create(user_id=new_id, user_name=name, user_email=email, user_password=password)
        return render(request, 'signIn.html', {'name': name})

"""
def logout_user(request): #no need
    logout(request)
    return redirect('home')
"""
