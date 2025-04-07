from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm, RecipeImageForm
from django.contrib.auth.decorators import login_required


@login_required
def recipe_list(request):
    '''
    View to list all recipes.
    '''
    recipes = Recipe.objects.all()

    return render(request, "recipe_list.html", {"recipes": recipes})

@login_required
def recipe_detail(request, pk):
    '''
    View to display a single recipe and its related images and ingredients.
    '''
    recipe = Recipe.objects.get(pk=pk)
    images = recipe.images.all()
    ingredients = recipe.ingredients.all()

    return render(request, "recipe_detail.html", {"recipe": recipe, "images": images, "ingredients": ingredients})

@login_required
def create_recipe(request):
    '''
    View for creating recipes, ingredients, and recipe ingredients.
    '''
    recipe_form = RecipeForm()
    ingredient_form = IngredientForm()
    recipe_ingredient_form = RecipeIngredientForm()

    if request.method == 'POST':
        if 'add_recipe' in request.POST:
            recipe_form = RecipeForm(request.POST)
            if recipe_form.is_valid():
                recipe = recipe_form.save(commit=False)
                recipe.author = request.user.profile
                recipe.save()
                return redirect('ledger:create_recipe')
        
        elif 'add_ingredient' in request.POST:
            ingredient_form = IngredientForm(request.POST)
            if ingredient_form.is_valid():
                ingredient_form.save()
                return redirect('ledger:create_recipe')
        
        elif 'add_recipe_ingredient' in request.POST:
            recipe_ingredient_form = RecipeIngredientForm(request.POST)
            if recipe_ingredient_form.is_valid():
                recipe_ingredient = recipe_ingredient_form.save()
                recipe = recipe_ingredient.recipe
                recipe.save()
                return redirect('ledger:create_recipe')
        
    return render(request, "new_recipe.html", {"recipe_form": recipe_form, "ingredient_form": ingredient_form, "recipe_ingredient_form": recipe_ingredient_form})

@login_required
def recipe_add_image(request, pk):
    '''
    View for adding images to recipes.
    '''
    recipe = Recipe.objects.get(pk=pk)
    recipe_image_form = RecipeImageForm()
    if request.method == 'POST':
        recipe_image_form = RecipeImageForm(request.POST, request.FILES)
        if recipe_image_form.is_valid():
            recipe_image = recipe_image_form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            recipe.save()
            return redirect('ledger:recipe_detail', pk=pk)
    
    return render(request, "new_image.html", {"recipe": recipe, "recipe_image_form": recipe_image_form})