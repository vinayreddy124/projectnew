from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        USERS = 'USERS', 'User'
        DEALER = 'DEALER', 'Dealer'

    is_dealer = models.BooleanField(default=False)
    role = models.CharField(max_length=6, choices=Role.choices, default=Role.USERS)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=300,default='')
    dealer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True) 

    def _str_(self):
        return f"Wishlist for {self.user.username}"