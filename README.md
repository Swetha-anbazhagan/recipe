#  ✅Assignment 1

## 📅Date: 09/07/2025

### You’re building a recipe app. Design models for Recipe and Ingredient. A recipe can have many ingredients. Include quantity as an extra field using a through model.

## Program

 models.py

 ```
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

```
## Outputs

![Screenshot 2025-07-09 123629](https://github.com/user-attachments/assets/3969cf70-a8cd-4b88-8b75-6986b6027a70)

![Screenshot 2025-07-09 123643](https://github.com/user-attachments/assets/6bd06085-27cf-4a48-91f1-9fe04d5bee11)

![Screenshot 2025-07-09 123656](https://github.com/user-attachments/assets/5ec91f3e-8640-42a7-9c2e-f560f5e1c5c1)

![Screenshot 2025-07-09 123715](https://github.com/user-attachments/assets/0b9e153e-fac3-4168-a161-2b5f7aa4df40)

![Screenshot 2025-07-09 123734](https://github.com/user-attachments/assets/a8d6d886-5388-46e8-b587-5d722526ba3d)


