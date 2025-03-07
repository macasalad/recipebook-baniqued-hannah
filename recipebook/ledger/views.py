from django.shortcuts import render
from .models import Recipe

def recipes(request):
    '''
    View to list all recipes.
    '''
    recipes = Recipe.objects.all()
    ctx = {
        "recipes":recipes
    }

    return render(request, "recipes.html", ctx)

def recipe(request, pk):
    '''
    View to display a single recipe and its ingredients.
    '''
    recipe = Recipe.objects.get(pk = pk)
    ingredients = recipe.ingredients.all()
    ctx = {
        "recipe":recipe,
        "ingredients":ingredients
    }

    return render(request, "recipe.html", ctx)