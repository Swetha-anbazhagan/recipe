from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient

# This allows you to edit ingredients directly inside the Recipe admin page
class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient
    extra = 1  # how many blank rows to show for new ingredients

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]  # add the inline section

# Register your models
admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)

