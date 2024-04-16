from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name='user_login'),
    path('user_home/', views.user_home, name='user_home'),
    path('product_list/', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('updateproduct/<int:id>/', views.updateproduct, name='updateproduct'),
    path('deleteProduct/<int:product_id>/', views.deleteProduct, name='deleteProduct'),
    path('deletewishlist/<int:wishlist_id>/', views.deletewishlist, name='deletewishlist'),
    path('addwishlist/<int:product_id>/', views.addwishlist, name='addwishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),

    
] 