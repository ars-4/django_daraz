from django.shortcuts import render
from django.http import HttpResponse
from core.decorators import multi_role
from django.contrib.auth.models import User, Group
from core.models import Person, Shop, Product, Picture
from django.contrib.auth.decorators import login_required

# Create your views here.

@multi_role(allowed_roles=['admin'])
def index(request):
    return HttpResponse("The")


@login_required(login_url='LoginPage')
def user_page(request):
    user = User.objects.get(id=request.user.id)
    person = Person.objects.get(username=user)
    context = {
        'user':user,
        'person':person
    }
    return render(request, 'user/user_home_page.html', context)

