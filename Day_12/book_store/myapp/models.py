from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField()
    phone_number = models.CharField()
    
    def __str__(self):
        return f"Name of Customer: {self.name}"


class Book(models.Model):
    name = models.CharField()
    author = models.CharField()

    def __str__(self):
        return f"Name of Book: {self.name}"