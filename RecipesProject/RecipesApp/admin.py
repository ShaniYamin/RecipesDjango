from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(RecipeIngredientsLine)
admin.site.register(Tag)
admin.site.register(Recipe)