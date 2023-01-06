from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from core.decorators import user_logged_in
from django.http import HttpResponse

# Create your views here.


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('UserPage')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('UserPage')
    return render(request, 'auth/login_page.html')



def Logout(request):
    logout(request)
    return redirect('LoginPage')

