from django.contrib import admin
from .models import Category


# admin.site.register(Category)
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('Appartements', 'FoodAndLife', 'Cars', 'Shopping', 'Travelling', 'is_deleted')
