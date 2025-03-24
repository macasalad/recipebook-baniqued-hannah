from django.shortcuts import render
from .models import Recipe
from django.contrib.auth.decorators import login_required

@login_required
def recipes(request):
    '''
    View to list all recipes.
    '''
    recipes = Recipe.objects.all()
    ctx = {
        "recipes": recipes
    }

    return render(request, "recipes.html", ctx)

@login_required
def recipe(request, pk):
    '''
    View to display a single recipe and its ingredients.
    '''
    recipe = Recipe.objects.get(pk = pk)
    ingredients = recipe.ingredients.all()
    images = recipe.images.all()
    ctx = {
        "recipe": recipe,
        "images": images,
        "ingredients": ingredients,
    }

    return render(request, "recipe.html", ctx)