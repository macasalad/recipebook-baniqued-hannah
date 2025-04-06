from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm, IngredientForm, RecipeIngredientForm
from django.contrib.auth.decorators import login_required

@login_required
def recipe_list(request):
    '''
    View to list all recipes.
    '''
    recipes = Recipe.objects.all()
    
    ctx = {
        "recipes": recipes
    }
    return render(request, "recipe_list.html", ctx)

@login_required
def recipe_detail(request, pk):
    '''
    View to display a single recipe and its related images and ingredients.
    '''
    recipe = Recipe.objects.get(pk = pk)
    images = recipe.images.all()
    ingredients = recipe.ingredients.all()

    ctx = {
        "recipe": recipe,
        "images": images,
        "ingredients": ingredients,
    }
    return render(request, "recipe_detail.html", ctx)

@login_required
def create_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        recipe_ingredient_form = RecipeIngredientForm(request.POST)
        
        if recipe_form.is_valid() and recipe_ingredient_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user.profile
            recipe.save()
            
            recipe_ingredient = recipe_ingredient_form.save(commit=False)
            recipe_ingredient.recipe = recipe
            recipe_ingredient.save()
            
            return redirect('ledger:create_recipe')
    else:
        recipe_form = RecipeForm()
        recipe_ingredient_form = RecipeIngredientForm()
    
    ctx = {
        "recipe_form": recipe_form,
        "recipe_ingredient_form": recipe_ingredient_form
    }
    return render(request, "new_recipe.html", ctx)
# def create_recipe(request):
#     # Form for new recipe
#     recipe_form = RecipeForm()
#     if request.method == 'POST':
#         recipe_form = RecipeForm(request.POST)
#         if recipe_form.is_valid():
#             recipe = recipe_form.save(commit=False)
#             recipe.author = request.user.profile
#             recipe.save()
#             return redirect('ledger:create_recipe')
    
#     # Form for new recipe ingredient
#     recipe_ingredient_form = RecipeIngredientForm()
#     if request.method == 'POST':
#         recipe_ingredient_form = RecipeIngredientForm(request.POST)
#         if recipe_ingredient_form.is_valid():
#             recipe_ingredient = recipe_ingredient_form.save(commit=False)
#             recipe_ingredient.save()
#             return redirect('ledger:create_recipe')
    
#     ctx = {
#         "recipe_form": recipe_form,
#         "recipe_ingredient_form": recipe_ingredient_form
#     }
#     return render(request, "new_recipe.html", ctx)

@login_required
def create_ingredient(request):
    if request.method == 'POST':
        ingredient_form = IngredientForm(request.POST)
        if ingredient_form.is_valid():
            ingredient_form.save()
            return redirect('ledger:create_recipe')
    else:
        ingredient_form = IngredientForm()
    
    ctx = {
        "ingredient_form": ingredient_form
    }
    return render(request, "new_ingredient.html", ctx)
# def create_ingredient(request):
#     # Form for new ingredient
#     ingredient_form = IngredientForm()
#     if request.method == 'POST':
#         ingredient_form = IngredientForm(request.POST)
#         if ingredient_form.is_valid():
#             ingredient = ingredient_form.save(commit=False)
#             ingredient.save()
#             return redirect('ledger:create_recipe')
#     ctx = {
#         "ingredient_form": ingredient_form
#     }
    
#     return render(request, "new_ingredient.html", ctx)