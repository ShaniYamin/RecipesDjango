from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    
class Recipe(models.Model):
    recipe_name= models.CharField(max_length=300)
    author_name= models.CharField(max_length=200)
    category= models.CharField(max_length=200)
    prep_time= models.IntegerField()
    cook_time= models.IntegerField()
    total_time= models.IntegerField()
    servings= models.IntegerField()
    ingredients= models.TextField()
    instructions = models.TextField()
    tips= models.TextField()
    tags= models.TextField(default=None)
    # image = models.ImageField(upload_to='static/recipe_images/', null=True, blank=True)

    def set_ingredients(self, ingredients_list):
        self.ingredients = '\n'.join(ingredients_list)

    def get_ingredients(self):
        return self.ingredients.split('\n')
    
    def set_instructions(self, instructions_list):
        self.instructions = '\n'.join(instructions_list)

    def get_instructions(self):
        return self.instructions.split('\n')
    
    def set_tips(self, tips_list):
        self.tips = '\n'.join(tips_list)

    def get_tips(self):
        return self.tips.split('\n')
    
    def set_tags(self, tags_list):
        self.tags = ','.join(tags_list)

    def get_tags(self):
        return self.tags.split(',')
    
    def __str__(self):
      return self.recipe_name + ' by ' + self.author_name

    