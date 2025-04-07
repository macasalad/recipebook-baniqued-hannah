from django import forms
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage

class RecipeForm(forms.ModelForm):
    '''
    This is a form for creating or editing a recipe.
    '''
    class Meta:
        '''
        Meta configuration for RecipeForm.
        Uses the Recipe model and excludes the 'author' field.
        '''
        model = Recipe
        exclude = ['author']

class IngredientForm(forms.ModelForm):
    '''
    This is a form for creating or editing an ingredient.
    '''
    class Meta:
        '''
        Meta configuration for IngredientForm.
        It uses all fields from the Ingredient model.
        '''
        model = Ingredient
        fields = '__all__'

class RecipeIngredientForm(forms.ModelForm):
    '''
    This is a form for linking an Ingredient to a Recipe with a specific quantity.
    It allows selection of both Ingredient and Recipe from dropdowns.
    '''
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all())
    recipe = forms.ModelChoiceField(queryset=Recipe.objects.all())

    class Meta:
        '''
        Meta configuration for RecipeIngredientForm.
        Uses all fields from the RecipeIngredient model.
        '''
        model = RecipeIngredient
        fields = '__all__'

class RecipeImageForm(forms.ModelForm):
    '''
    This is a form for uploading an image related to a Recipe.
    '''
    class Meta:
        '''
        Meta configuration for RecipeImageForm.
        Uses the RecipeImage model and excludes the 'recipe' field.
        '''
        model = RecipeImage
        exclude = ['recipe']
