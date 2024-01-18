from django.db import models
from django import forms

# Create your models here.
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    bio = models.TextField(default=None)
    email = models.EmailField(default=None)

    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=100)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label
    

class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    def __str__(self):
        return self.label 
    
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    
    def __str__(self):
        return self.label
    
    
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=300)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,default=None,related_name='authorOfRecipe')
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    total_time = models.IntegerField()
    servings = models.IntegerField()
    difficulty = models.CharField(max_length=300,default=None)
    ingredients = models.ManyToManyField(Ingredient, related_name='IngredientsForRecipe', through='RecipeIngredientsLine')
    instructions = models.JSONField(default=list)
    tips = models.JSONField(default=list)
    tags = models.ManyToManyField(Tag)
    # image = models.ImageField(upload_to='static/recipe_images/', null=True, blank=True)
    
    # def add_tag(self, tag_name):
    #     tag = Recipe.get_or_create_tag(tag_name)
    #     self.tags.add(tag)

    # def add_ingredient(self, ingredient_name, quantity):
    #     ingredient = Recipe.create_or_get_ingredient(ingredient_name)
    #     Quantity.objects.create(recipe=self, ingredient=ingredient, quantity=quantity)

    
    def __str__(self):
      return f"{self.recipe_name} by {self.author.name}"

class RecipeIngredientsLine(models.Model):
    id = models.AutoField(primary_key=True)
    recipe=models.ForeignKey(Recipe,  on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE )
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    
    def __str__(self):
        return f"{self.quantity} {self.unit.label} of {self.ingredient.label}"  
    
