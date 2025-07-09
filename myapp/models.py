# models.py

from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.title}"

