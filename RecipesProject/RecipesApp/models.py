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
    
class Quantity(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=100)
    
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=300)
    author_name = models.ForeignKey(Author,related_name='RecipeAuthorName' ,on_delete=models.CASCADE)
    author_email = models.ForeignKey(Author,related_name='RecipeAuthorEmail', on_delete=models.CASCADE)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    total_time = models.IntegerField()
    servings = models.IntegerField()
    difficulty = models.CharField(max_length=300,default=None)
    ingredients = models.ManyToManyField(Ingredient, through='Quantity')
    instructions = models.JSONField(default=list)
    tips = models.JSONField(default=list)
    tags = models.ManyToManyField(Tag)
    # image = models.ImageField(upload_to='static/recipe_images/', null=True, blank=True)

    def set_instructions(self, instructions_list):
        self.instructions = instructions_list

    def get_instructions(self):
        return self.instructions

    def set_tips(self, tips_list):
        self.tips = tips_list

    def get_tips(self):
        return self.tips
    
    @classmethod
    def get_or_create_tag(cls, tag_name):
        tag, created = Tags.objects.get_or_create(tag=tag_name)
        return tag

    @classmethod
    def get_or_create_author(cls, author_name, bio, email):
        author, created = Author.objects.get_or_create(name=author_name, bio=bio, email=email)
        return author
    
    def add_category(self, category_name):
        category = Recipe.get_or_create_category(category_name)
        self.categorys.add(category)

    def add_tag(self, tag_name):
        tag = Recipe.get_or_create_tag(tag_name)
        self.tags.add(tag)

    def add_ingredient(self, ingredient_name, quantity):
        ingredient = Recipe.create_or_get_ingredient(ingredient_name)
        Quantity.objects.create(recipe=self, ingredient=ingredient, quantity=quantity)

    
    def __str__(self):
      return f"{self.recipe_name} by {self.author_name}"
