#from django.conf.urls import include, url, patterns # - не сущ-ет?
#import views

#urlpatterns = patterns('',
    #url(r'^$', views.ListRecipeView.as_view(), # $- замыкающий символ
      #  name='recipes-list',),
#)

#from django.contrib import admin
#from django.urls import path, include #new

#urlpatterns = [
  #  path('admin/', admin.site.urls),
   # path('recipes', include('recipes.urls')) #new
#]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('signIn', views.signIn, name = 'signIn'), #здесь просто перечислены все url принадлежащие приложению и на какой view они ссылаются
]