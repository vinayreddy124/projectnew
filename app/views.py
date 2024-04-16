from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProductForm, WishlistForm
from .models import User, Product, Wishlist
from django.shortcuts import render, redirect, get_object_or_404



def homepage(request):
    return render(request, 'homepage.html')

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = User.Role.DEALER if form.cleaned_data['is_dealer'] else User.Role.USERS
            user.save()
            login(request, user)
            return redirect('product_list' if user.role == User.Role.DEALER else 'user_home')
    else:
        form = RegistrationForm()
    
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('product_list' if user.role == User.Role.DEALER else 'user_home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_home(request):
    products = Product.objects.all()
    return render(request, 'user.html',{'products':products})


def product_list(request):
    products = Product.objects.filter(dealer=request.user)
    return render(request, 'productlist.html', {'products': products})

#to add product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.dealer = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'addproduct.html', {'form': form})

  
#to update a product
def updateproduct(request, id):
    obj = Product.objects.get(pk=id)
    form = ProductForm(instance=obj)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request, 'updateproduct.html', {'form': form})
    

#to delete a product
def deleteProduct(request, product_id):
    product = get_object_or_404(Product, pk=product_id) 
    if request.method == 'POST':
        product.delete() 
        return redirect('product_list')
    else:
        return render(request, 'deleteproduct.html', {'product': product})

    

def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})



#to add wishlist
def addwishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = WishlistForm(request.POST)
        if form.is_valid():
            wishlist = form.save(commit=False)
            wishlist.user = request.user
            wishlist.save()  

            wishlist.products.add(product)  

            return redirect('wishlist')  
    else:
        form = WishlistForm()

    return render(request, 'addwishlist.html', {'form': form, 'product': product})

#to delete a wishlist
def deletewishlist(request, wishlist_id):
    wishlist = get_object_or_404(Wishlist, pk=wishlist_id)
    
    if request.method == 'POST':
        wishlist.delete()
        return redirect('wishlist') 
    
    return render(request, 'deletewishlist.html', {'wishlist': wishlist})
