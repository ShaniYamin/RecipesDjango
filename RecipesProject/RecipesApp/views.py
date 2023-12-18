from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe
from rest_framework import serializers,viewsets,status

from .forms import CreateRecipeForm

@api_view(['GET'])
def home(request):
    return Response({"message":'Welcome to my Recipes Website'})

class Recipes(viewsets.ViewSet):
    def list(self,request):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response({"recipes": serializer.data}, status=status.HTTP_200_OK)
    def create(self,request):
        r= Recipe(recipe_name=request.data.get('recipeName'),
            author_name=request.data.get('authorName'),
            category=request.data.get('category'),
            prep_time=request.data.get('prepTime'),
            cook_time=request.data.get('cookTime'),
            total_time=request.data.get('totalTime'),
            servings=request.data.get('servings'),
            ingredients=request.data.get('ingredients'),
            instructions=request.data.get('instructions'),
            tips=request.data.get('tips'),
            tags=request.data.get('tags'))
        r.save()
        return Response({"message":"created new recipe"},status.HTTP_201_CREATED)
    def destroy(self, request, pk=None):
        Recipe.objects.filter(id=pk).delete()
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response({"recipes": serializer.data}, status.HTTP_200_OK)
        
def createRecipe(request):
    form= CreateRecipeForm()
    if request.method == 'POST':
        form= CreateRecipeForm(request.POST)
        if form.is_valid():
            form.save();
    context={"form":form}
    return render(request,'createRecipe.html',context)

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

