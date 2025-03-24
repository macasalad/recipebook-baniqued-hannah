from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage

class RecipeIngredientInline(admin.TabularInline):
    '''
    Inline admin for RecipeIngredient
    '''
    model = RecipeIngredient

    extra = 0

class RecipeImageInline(admin.TabularInline):
    '''
    Inline admin for RecipeImage
    '''
    model = RecipeImage

    extra = 0

class IngredientAdmin(admin.ModelAdmin):
    '''
    Admin configuration for Ingredient model
    '''
    model = Ingredient

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    '''
    Admin configuration for Recipe model
    '''
    model = Recipe

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    inlines = [RecipeIngredientInline, RecipeImageInline,]

class RecipeIngredientAdmin(admin.ModelAdmin):
    '''
    Admin configuration for RecipeIngredient model
    '''
    model = RecipeIngredient

    list_display = ('recipe', 'ingredient', 'quantity',)
    list_filter = ('recipe', 'ingredient',)
    search_fields = ('name',)

class ProfileInline(admin.TabularInline):
    '''
    Inline admin configuration for the Profile model
    '''
    model = Profile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    '''
    Custom admin configuration for the User model.
    '''
    inlines = [ProfileInline,]

# Register models with their corresponding admin configurations
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)

# Models for user management
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)