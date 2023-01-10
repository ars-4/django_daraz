from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginPage, name='LoginPage'),
    path('register/', views.sign_up, name='SignUpPage'),
    path('logout/', views.Logout, name='LogoutPage'),

    path('403/', views.forbidden_view, name='ForbiddenPage')

]
