from django.urls import path
from core import views

urlpatterns = [
    path('dashboard/', views.index, name='IndexPage'),
    path('', views.index),
    path('home/', views.home_page, name='HomePage'),

    path('user/', views.user_page, name='UserPage'),
    path('user/<str:username>/', views.user_read_page, name='UserByUsername'),

    path('store/', views.store_view, name='StorePage'),

    path('product/create/', views.create_product, name='CreateProductPage'),
    path('product/<str:pk>/', views.read_product, name='ReadProductPage')
]