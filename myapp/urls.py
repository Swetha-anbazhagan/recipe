from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('create/', views.create_recipe, name='create_recipe'),
    path('edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
]
