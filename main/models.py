from operator import mod
from statistics import mode
from django.db import models

# Create your models here.
class TestModel(models.Model):
    title = models.CharField(max_length=40)