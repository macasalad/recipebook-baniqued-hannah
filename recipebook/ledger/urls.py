from django.urls import path
from .views import recipes, recipe

urlpatterns = [
    path('recipes/list/', recipes, name="recipe_list"),
    path('recipe/<int:pk>/', recipe, name="recipe_detail")
]

app_name = 'ledger'