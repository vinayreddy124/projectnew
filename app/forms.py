from django import forms
from .models import User, Product, Wishlist

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_dealer']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price','image']

class WishlistForm(forms.ModelForm):
  
    class Meta:
        model = Wishlist
        fields = []