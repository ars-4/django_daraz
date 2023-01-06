from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginPage, name='LoginPage'),
    path('logout/', views.Logout, name='LogoutPage')
]
