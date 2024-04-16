from django.contrib import admin
from .models import User, Product, Wishlist

admin.site.register(User)
admin.site.register(Product)  
admin.site.register(Wishlist)