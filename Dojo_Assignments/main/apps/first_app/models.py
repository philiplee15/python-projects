from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Produce(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 255)
    weight = models.IntegerField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_print = models.BooleanField(default=True)
