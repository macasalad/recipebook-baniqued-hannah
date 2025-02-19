from django.urls import path
from .views import recipes, recipe1

urlpatterns = [
    path('recipes/list', recipes, name = "Recipe Book"),
    path('recipe/1/', recipe1, name = "Recipe 1"),
]

app_name = 'ledger'