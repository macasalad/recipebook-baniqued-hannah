from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Profile(models.Model):
    '''
    This is a model for individual users.
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=255)

    def __str__(self):
        '''
        String representation of the user's name
        '''
        return self.name

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
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

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

class RecipeImage(models.Model):
    '''
    This is a model for recipe images.
    '''
    image = models.ImageField(upload_to="recipe_images/")
    description = models.TextField(max_length=255)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_images")