# Generated by Django 4.0.2 on 2022-02-14 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.FloatField(help_text='the amount required to purchase for this recipe')),
                ('unit', models.CharField(help_text='The unit of measure referenced by quantity', max_length=100)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.recipe')),
            ],
            options={
                'ordering': ['recipe', 'ingredient'],
            },
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('intended_order_date', models.DateTimeField()),
                ('items', models.ManyToManyField(to='food.Ingredient')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='mealplan',
            name='friday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friday_recipe', to='food.recipe'),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='monday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monday_recipe', to='food.recipe'),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='saturday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saturday_recipe', to='food.recipe'),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='sunday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sunday_recipe', to='food.recipe'),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='thursday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thursday_recipe', to='food.recipe'),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='tuesday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tuesday_recipe', to='food.recipe'),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='wednesday',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wednesday_recipe', to='food.recipe'),
        ),
    ]
