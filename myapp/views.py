from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe, Ingredient, RecipeIngredient
from .forms import RecipeForm

# List all recipes
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})


# Create a new recipe
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            ingredient_ids = request.POST.getlist('ingredients')
            quantities = request.POST.getlist('quantities')

            for i_id, qty in zip(ingredient_ids, quantities):
                if i_id and qty:
                    RecipeIngredient.objects.create(
                        recipe=recipe,
                        ingredient_id=i_id,
                        quantity=qty
                    )
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    ingredients = Ingredient.objects.all()
    return render(request, 'create_recipe.html', {'form': form, 'ingredients': ingredients})


# Edit an existing recipe
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            RecipeIngredient.objects.filter(recipe=recipe).delete()

            ingredient_ids = request.POST.getlist('ingredients')
            quantities = request.POST.getlist('quantities')

            for i_id, qty in zip(ingredient_ids, quantities):
                if i_id and qty:
                    RecipeIngredient.objects.create(
                        recipe=recipe,
                        ingredient_id=i_id,
                        quantity=qty
                    )
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
        selected_ingredients = recipe.recipeingredient_set.all()
        ingredients = Ingredient.objects.all()

    return render(request, 'edit_recipe.html', {
        'form': form,
        'ingredients': ingredients,
        'recipe': recipe,
        'selected_ingredients': selected_ingredients
    })


# Delete a recipe
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    return redirect('recipe_list')
