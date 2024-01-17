from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe,Tag,Ingredient,Unit,Author,Quantity
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
        print(request.data)
        author,created_author =Author.objects.get_or_create(name=request.data.get('authorName'),email=request.data.get('authorEmail'))
        recipe = Recipe(recipe_name=request.data.get('recipeName'),
            author_name=author,
            author_email=author,
            prep_time=request.data.get('prepTime'),
            cook_time=request.data.get('cookTime'),
            total_time=request.data.get('totalTime'),
            servings=request.data.get('servings'),
            difficulty=request.data.get('difficulty'),
            instructions=request.data.get('instructions'),
            tips=request.data.get('tips'))
        recipe.save()
        ingredients = request.data.get('ingredients')
        for ingred in ingredients:
            unit_obj, created_unit = Unit.objects.get_or_create(value=ingred['unit'], label=ingred['unit'])
            ingredient_obj, created_ingredient = Ingredient.objects.get_or_create(value=ingred['ingredient'], label=ingred['ingredient'])
            quan=Quantity(unit=unit_obj,ingredient=ingredient_obj,quantity=ingred['quantity'])
            recipe.ingredients.add(quan)
        tags = request.data.get('tags')
        for tag in tags:
            tag_obj, created_tag = Tag.objects.get_or_create(value=tag.value,label=tag.label)
            recipe.Tag.add(tag_obj)
        recipe.save()
        return Response({"message":"created new recipe"},status.HTTP_201_CREATED)
    def destroy(self, request, pk=None):
        Recipe.objects.filter(id=pk).delete()
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response({"recipes": serializer.data}, status.HTTP_200_OK)

class Tags(viewsets.ViewSet):
     def list(self,request):
        tags = Tag.objects.all()
        serializer = tagsSerializer(tags, many=True)
        return Response({"tags": serializer.data}, status=status.HTTP_200_OK)

class Authors(viewsets.ViewSet):
     def list(self,request):
        authors = Author.objects.all()
        serializer = authorsSerializer(authors, many=True)
        return Response({"authors": serializer.data}, status=status.HTTP_200_OK)
    
class Ingredients(viewsets.ViewSet):
     def list(self,request):
        ingredients = Ingredient.objects.all()
        serializer = ingredientsSerializer(ingredients, many=True)
        return Response({"ingredients": serializer.data}, status=status.HTTP_200_OK)

class Units(viewsets.ViewSet):
     def list(self,request):
        units = Unit.objects.all()
        serializer = unitSerializer(units, many=True)
        return Response({"units": serializer.data}, status=status.HTTP_200_OK)
        
def createRecipe(request):
    form= CreateRecipeForm()
    if request.method == 'POST':
        form= CreateRecipeForm(request.POST)
        inForm= form.quantity_formset
        if form.is_valid():
            form.save();
    elif request.method == 'GET':
        form=CreateRecipeForm()
        inForm= form.quantity_formset
        context={"form":form,"inForm":inForm}
        return render(request,'createRecipe.html',context)
    context={"form":form,"inForm":inForm}
    return render(request,'createRecipe.html',context)

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
        
class tagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
        
class ingredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
        
class unitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'
        
class authorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
                

