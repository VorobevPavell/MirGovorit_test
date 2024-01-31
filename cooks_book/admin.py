from django.contrib import admin
from .models import Recipe, Products, RecipeProduct


admin.site.register(Recipe)
admin.site.register(Products)
admin.site.register(RecipeProduct)
