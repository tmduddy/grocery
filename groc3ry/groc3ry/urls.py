"""groc3ry URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [path("api/admin/", admin.site.urls), path("api/food/", include("food.urls"))]
