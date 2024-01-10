from django.urls import path
from . import views

urlpatterns = [ 
    path('home/',views.home,name='home'),
    path('recipes/', views.Recipes.as_view({'get': 'list','post': 'create','delete':'destroy'})),
    path('recipes/<int:pk>', views.Recipes.as_view({'delete':'destroy'})),
    path('createRecipe/',views.createRecipe,name='createRecipe'),
    path('tags/',views.Tags.as_view({'get': 'list'})),
    path('ingredients/',views.Ingredients.as_view({'get': 'list'})),
     path('units/',views.Units.as_view({'get': 'list'})),
]

