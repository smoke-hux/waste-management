from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class GarbageCollection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=[('organic', 'Organic'), ('inorganic', 'Inorganic')])
    weight = models.FloatField()
    earnings = models.FloatField()
