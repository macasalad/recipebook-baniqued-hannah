from django.urls import path
from .views import recipes

urlpatterns = [
    path('recipes/list/', recipes, name = "Recipe Book"),
]

app_name = 'ledger'