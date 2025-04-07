from django import forms
from .models import Recipe, Ingredient, RecipeIngredient, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeIngredientForm(forms.ModelForm):
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all())
    recipe = forms.ModelChoiceField(queryset=Recipe.objects.all())

    class Meta:
        model = RecipeIngredient
        fields = '__all__'

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        exclude = ['recipe']