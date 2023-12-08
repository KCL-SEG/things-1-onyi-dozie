from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

# class Thing(models.Model):
#     name = models.CharField(max_length=30,unique=True)
#     description = models.CharField(unique = False,max_length=120,blank = True)
#     quantity = models.IntegerField(unique = True,MaxValueValidator = 100,MinValueValidator = 0)