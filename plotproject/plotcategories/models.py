from django.db import models


class Category(models.Model):
    Appartements = models.CharField(max_length=30, default='')
    FoodAndLife = models.CharField(max_length=30, default='')
    Cars = models.CharField(max_length=30, default='')
    Shopping = models.CharField(max_length=30, default='')
    Travelling = models.CharField(max_length=30, default='')
    is_deleted = models.BooleanField(default=False)
