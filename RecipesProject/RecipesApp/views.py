from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe
from rest_framework import serializers


@api_view(['GET'])
def home(request):
    return Response({"message":'Home Page'})

@api_view(['GET'])
def recipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response({"recipes": serializer.data}, status=200)


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

