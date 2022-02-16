from django.db import models


class Ingredient(models.Model):
    """A base ingredient as would be purchased"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]


class Recipe(models.Model):
    """a collection of ingredients"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]


class RecipeIngredient(models.Model):
    """An instance of an ingredient belonging to a particular recipe (important for qty and units)"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quantity = models.FloatField(
        help_text="the amount required to purchase for this recipe"
    )
    unit = models.CharField(
        max_length=100, help_text="The unit of measure referenced by quantity"
    )
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    class Meta:
        ordering = ["recipe", "ingredient"]


class ShoppingList(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    intended_order_date = models.DateTimeField()
    items = models.ManyToManyField(Ingredient)

    class Meta:
        ordering = ["name"]


class MealPlan(models.Model):
    """A collection of recipes for a given week"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    sunday = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="sunday_recipe"
    )
    monday = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="monday_recipe"
    )
    tuesday = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="tuesday_recipe"
    )
    wednesday = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="wednesday_recipe"
    )
    thursday = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="thursday_recipe"
    )
    friday = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="friday_recipe"
    )
    saturday = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="saturday_recipe"
    )

    class Meta:
        ordering = ["updated_at"]
