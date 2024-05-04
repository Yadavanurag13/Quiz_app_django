from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

class Question(models.Model):
    category = 