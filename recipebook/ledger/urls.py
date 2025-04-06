from django.urls import path
from .views import recipe_list, recipe_detail, create_recipe, create_ingredient

urlpatterns = [
    path('recipes/list/', recipe_list, name="recipe_list"),
    path('recipe/<int:pk>/', recipe_detail, name="recipe_detail"),
    path('recipe/add/', create_recipe, name="create_recipe"),
    path('recipe/add/new-ingredient', create_ingredient, name="create_ingredient")
]

app_name = 'ledger'