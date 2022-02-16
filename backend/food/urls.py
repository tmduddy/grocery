from django.urls import path
from . import views

urlpatterns = [
    path("ingredient/", views.IngredientList.as_view()),
    path("ingredient/<int:pk>/", views.IngredientDetail.as_view()),
    path("recipe/", views.RecipeList.as_view()),
    path("recipe/<int:pk>/", views.RecipeDetail.as_view()),
    path("recipe_ingredient/", views.RecipeIngredientList.as_view()),
    path("recipe_ingredient/<int:pk>/", views.RecipeIngredientDetail.as_view()),
    path("shopping_list/", views.ShoppingListList.as_view()),
    path("shopping_list/<int:pk>/", views.ShoppingListDetail.as_view()),
    path("meal_plan/", views.MealPlanList.as_view()),
    path("meal_plan/<int:pk>/", views.MealPlanDetail.as_view()),
]
