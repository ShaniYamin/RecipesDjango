from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe

@api_view(['GET'])
def recipes(request):
    recipes=Recipe.objects.all()
    item_dic={"recipes":recipes}
    return Response(item_dic)

@api_view(['GET'])
def home(request):
    return Response({"message":'Home Page'})

