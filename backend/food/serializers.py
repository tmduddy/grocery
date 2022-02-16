from rest_framework import serializers
from food.models import Ingredient, RecipeIngredient, Recipe, ShoppingList, MealPlan


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"

    def create(self, validated_data):
        return Ingredient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"

    def create(self, validated_data):
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class RecipeIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeIngredient
        fields = "__all__"

    def create(self, validated_data):
        return RecipeIngredient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get("quantity", instance.quantity)
        instance.unit = validated_data.get("unit", instance.unit)
        instance.ingredient = validated_data.get("ingredient", instance.ingredient)
        instance.recipe = validated_data.get("recipe", instance.recipe)
        instance.save()
        return instance


class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = "__all__"

    def create(self, validated_data):
        return ShoppingList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.intended_order_date = validated_data.get(
            "intended_order_date", instance.intended_order_date
        )
        instance.save()
        return instance


class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = "__all__"

    def create(self, validated_data):
        return MealPlan.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.sunday = validated_data.get("sunday", instance.sunday)
        instance.monday = validated_data.get("monday", instance.monday)
        instance.tuesday = validated_data.get("tuesday", instance.tuesday)
        instance.wednesday = validated_data.get("wednesday", instance.wednesday)
        instance.thursday = validated_data.get("thursday", instance.thursday)
        instance.friday = validated_data.get("friday", instance.friday)
        instance.nasaturdayme = validated_data.get("saturday", instance.saturday)
        instance.save()
        return instance
