from django.urls import path
from . import views

urlpatterns = [
    #path('', views.InfoView.as_view()), # test
    path('', views.MainView.as_view()), #main.html
    path('allrecipes', views.RecipesInfoView.as_view()), # will be deleted (test) norecipe.html
    path('anton', views.UserInfoView.as_view()), # will be deleted (test) nouser.html
    path('reg', views.RegistaratoinView.as_view()), # reg.html
    path('signin', views.SignInView.as_view()), # signIn.html
    path('navigation', views.NavigationView.as_view()), # navigation.html
]