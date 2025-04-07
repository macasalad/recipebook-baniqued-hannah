from django.urls import path
from .views import recipe_list, recipe_detail, create_recipe, recipe_add_image


urlpatterns = [
    path('recipes/list/', recipe_list, name="recipe_list"),
    path('recipe/<int:pk>/', recipe_detail, name="recipe_detail"),
    path('recipe/add/', create_recipe, name="create_recipe"),
    path('recipe/<int:pk>/add_image/', recipe_add_image, name="recipe_add_image")
]

app_name = 'ledger'