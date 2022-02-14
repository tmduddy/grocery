from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)


class Ingredient(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
