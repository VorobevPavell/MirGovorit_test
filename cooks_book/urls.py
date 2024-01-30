from django.urls import path
from .views import show_home_page, AddProductToRecipe, CookRecipe, ShowRecipesWithoutProduct


urlpatterns = [
    path('', show_home_page, name="home"),
    path('add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>/', AddProductToRecipe.as_view(), name="add_product"),
    path('cook_recipe/<int:recipe_id>/', CookRecipe.as_view(), name="cook_recipe"),
    path('show_recipes_without_product/<int:product_id>', ShowRecipesWithoutProduct.as_view(), name="recipies")
]
