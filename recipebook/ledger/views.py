from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm
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

@login_required
def add_recipe(request):
    recipe_form = RecipeForm()
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user.profile
            recipe.save()
            return redirect('ledger:recipe_detail', pk=recipe.pk)

    ctx = {
        "recipe_form": recipe_form
    }
    return render(request, "add_recipe.html", ctx)