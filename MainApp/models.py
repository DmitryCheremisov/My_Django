from django.db import models

# Create your models here.

class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()
   color = models.CharField(max_length=30, default=None, blank=True)

   def __str__(self):
      return f"Item: {self.name} {self.brand} count: {self.count}"