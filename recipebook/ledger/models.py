from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient_detail', args=[self.pk])

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[self.pk])
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredient = models.ForeignKey(Ingredient, default=1, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, default=1, on_delete=models.CASCADE, related_name="ingredients")

    class Meta:
        verbose_name_plural = "Recipe Ingredients"