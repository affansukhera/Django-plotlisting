from django.db import models


class MyListing(models.Model):

    TYPE_CHOICES = [
        ('car', 'car'),
        ('appartements', 'appartements'),
        ('shopping', 'shopping'),
        ('travelling', 'travelling'),
        ('foodandlife', 'foodandlife'),
    ]
    area = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    location = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='images/', default='')
    title = models.CharField(max_length=100, default='')
    listing_type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    is_deleted = models.BooleanField(default=False)


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    car = models.BooleanField(default=False)
    appartements = models.BooleanField(default=False)
    shopping = models.BooleanField(default=False)
    travelling = models.BooleanField(default=False)
    foodandlife = models.BooleanField(default=False)
    message = models.TextField()
