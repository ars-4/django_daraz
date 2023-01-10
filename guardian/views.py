from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from core.decorators import user_logged_in
from django.http import HttpResponse
from guardian.forms import CustomUserCreationForm
from core.models import Person
from django.contrib.auth.models import Group

# Create your views here.


def forbidden_view(request):
    return render(request, 'ErrorPages/forbidden_page.html')


def not_found_view(request, exception):
    return render(request, 'ErrorPages/not_found_page.html', status=404)



def sign_up(request):
    if request.user.is_authenticated:
        return redirect('UserPage')
    else:
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.groups.add(Group.objects.get(name='buyer'))
                person = Person.objects.create(
                    username=user,
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address']
                )
                person.save()
                print(user)
                print(person)
                return redirect('LoginPage')

        context = {
            'form':form
        }
        return render(request, 'auth/signup_page.html', context)

def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('HomePage')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('HomePage')
    return render(request, 'auth/login_page.html')

def Logout(request):
    logout(request)
    return redirect('LoginPage')

