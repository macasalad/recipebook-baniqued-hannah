from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    '''
    This is a model for individual ingredients.
    '''
    name = models.CharField(max_length=50)

    def __str__(self):
        '''
        String representation of the ingredient name
        '''
        return self.name
    
    def get_absolute_url(self):
        '''
        Returns the URL for the ingredient's detail page
        '''
        return reverse('ledger:ingredient_detail', args=[self.pk])

class Recipe(models.Model):
    '''
    This is a model for recipes.
    '''
    name = models.CharField(max_length=50)

    def __str__(self):
        '''
        String representation of the recipe name
        '''
        return self.name
    
    def get_absolute_url(self):
        '''
        Returns the URL for the recipe's detail page
        '''
        return reverse('ledger:recipe_detail', args=[self.pk])
    
class RecipeIngredient(models.Model):
    '''
        This is a model for linking ingredients to recipes
    '''
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, default=1, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, default=1, on_delete=models.CASCADE, related_name="ingredients")

    class Meta:
        '''
        Customizing the plural name in the admin interface
        '''
        verbose_name_plural = "Recipe Ingredients"