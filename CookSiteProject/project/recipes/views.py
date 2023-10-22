from django.shortcuts import render,   redirect

# Create your views here.

from django.views.generic import ListView

from .models import RecipeModel
from django.http import HttpResponse


def index(request):  # new
      get_recipes = RecipeModel.objects.all()
      return render(request, 'recipes/norecipe.html', {'get_recipes': get_recipes})


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def signIn(request):
      if request.method == 'POST':
            name = request.POST.get('name')
            password = request.POST.get('password')
            user = authenticate(request, name=name, password=password)
            if user is not None:
                  if user.is_active:
                        login(request, user)
                        return redirect('home')
            else:
                  messages.info(request, 'Имя пользователя или пароль введены неправильно')
      context = {}
      return render(request, 'recipes/signIn.html', context)

def logout_user(request):
    logout(request)
    return redirect('home')




#https://habr.com/ru/articles/242261/
#class ListRecipeView(ListView):
#       model = RecipeModel
#      template_name = 'norecipe.html'

            #HttpResponse(template_name) #('<h1>Django Include URLs</h1>')

# https://codinggear.blog/django-include-urls/
#from django.http import HttpResponse #new
#