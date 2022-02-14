from django.urls import path
from . import views

urlpatterns = [path("ingredient/", views.IngredientViewSet.as_view())]
