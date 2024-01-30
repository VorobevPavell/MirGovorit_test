from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Products, Recipe, RecipeProduct
from django.db.models import Q


def show_home_page(request):
    return render(request, "base.html")


class AddProductToRecipe(View):

    @staticmethod
    def get(request, recipe_id, product_id, weight):
        """
        Добавляет к указанному рецепту
        указанный продукт с указанным весом.
        Если в рецепте уже есть такой продукт, то функция меняет его вес в этом рецепте на указанный.
        """
        recipe = Recipe()
        recipe_product = RecipeProduct()
        recipe.id = recipe_id
        recipe.save()

        finded = RecipeProduct.objects.filter(product=product_id, recipe=recipe_id).first()
        if finded:
            finded.weight = weight
            finded.save()
        else:
            recipe_product.recipe = Recipe.objects.filter(id=recipe_id).first()
            recipe_product.product = Products.objects.filter(id=product_id).first()
            recipe_product.weight = weight
            recipe_product.save()

        return HttpResponse(f"В рецепт {recipe_id} успешно добавлен продукт {product_id} весом {weight}")


class CookRecipe(View):

    @staticmethod
    def get(request, recipe_id):
        """
        Увеличивает на единицу количество приготовленных блюд для каждого продукта,
        входящего в указанный рецепт.
        """
        products_id_list = []
        products = RecipeProduct.objects.filter(recipe=recipe_id)
        for product in products:
            products_id_list.append(product.product_id)

        for used in products_id_list:
            used_product = Products.objects.filter(id=used).first()
            used_product.counter += 1
            used_product.save()
        return HttpResponse("success")


class ShowRecipesWithoutProduct(View):

    @staticmethod
    def get(request, product_id):
        """
         Функция возвращает HTML страницу, на которой размещена таблица. В таблице отображены id
         и названия всех рецептов,
         в которых указанный продукт отсутствует, или присутствует в количестве меньше 10 грамм.
        """
        recipes_names = {}

        recipes_without_product = RecipeProduct.objects.filter(
            Q(product=product_id) & (Q(weight__lt=10) | Q(weight__isnull=True))
        ).select_related('recipe')

        for product in recipes_without_product:
            recipes_names[product.recipe_id] = product.recipe.name

        context = {
            'product_id': product_id,
            'recipies': recipes_names
        }

        return render(request, "recipes_without_product.html", context=context)
