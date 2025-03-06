from django.shortcuts import render
from .models import Recipe, Ingredient, RecipeIngredient

def recipes(request):
    recipes = Recipe.objects.all()
    ctx = {
        "recipes" : recipes
    }
    return render(request, "recipes.html", ctx)

def recipe(request, pk):
    recipe = Recipe.objects.get(pk = pk)
    ingredients = recipe.ingredients.all()
    ctx = {
        "recipe": recipe,
        "ingredients" : ingredients
    }
    return render(request, "recipe.html", ctx)