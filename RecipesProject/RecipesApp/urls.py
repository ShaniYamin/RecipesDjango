from django.urls import path
from . import views

urlpatterns = [
    path('recipes/', views.recipes,name='recipes'),
    path('home/',views.home,name='home'),
    path('recipesCreate/',views.recipesCreate,name='recipesCreate'),
]