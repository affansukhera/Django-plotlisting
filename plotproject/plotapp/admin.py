from django.contrib import admin
from .models import MyListing, Contact


@admin.register(MyListing)
class Mylisting(admin.ModelAdmin):
    list_display = ('area', 'price', 'location', 'image', 'title', 'listing_type', 'is_deleted')


@admin.register(Contact)
class Mycontact(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'car', 'appartements', 'shopping', 'travelling', 'foodandlife', 'message')
