from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    is_verified = models.BooleanField(default=False)
    
    
from django.db import models

class User_info(models.Model):
    username = models.CharField(max_length=100, unique=True)
    cash_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    organic_garbage_collected = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    inorganic_garbage_collected = models.DecimalField(max_digits=10, decimal_places=2, default=0)
