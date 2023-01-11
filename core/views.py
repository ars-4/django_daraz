from django.shortcuts import render, redirect
from django.http import HttpResponse
from core.decorators import multi_role
from django.contrib.auth.models import User, Group
from core.models import Person, Shop, Product, Picture
from django.contrib.auth.decorators import login_required
from core.forms import PersonUpdateForm, ShopForm
from core.utils import get_or_create_shop, add_image, update_shop

# Create your views here.


# Dashboard
@login_required(login_url='LoginPage')
@multi_role(allowed_roles=['admin'])
def index(request):
    return HttpResponse("The")

# Home
@login_required(login_url='LoginPage')
def home_page(request):
    products = Product.objects.all()
    pictures = Picture.objects.all()
    context = {
        'products': products,
        'pictures': pictures
    }
    return render(request, 'dashboard/home_page.html', context)




# User
@login_required(login_url='LoginPage')
def user_read_page(request, username):
    user = User.objects.get(username=username)
    person = Person.objects.get(username=user)
    if person.username.groups.all()[0].name == 'seller':
        shop = get_or_create_shop(person)
    if shop.images:
        shop_images = shop.images.all().order_by('-id')[:3]

    context = {
        'person':person,
        'user': user,
        'store': shop,
        'shop_images': shop_images
    }
    if request.user.id == user.id:
        return redirect('UserPage')
    else:
        return render(request, 'user/user_home_page.html', context)


@login_required(login_url='LoginPage')
def user_page(request):
    user = User.objects.get(id=request.user.id)
    person = Person.objects.get(username=user)
    form = PersonUpdateForm(instance=person)

    if person.username.groups.all()[0].name == 'seller':
        shop = get_or_create_shop(person)
    
    if shop.images:
        shop_images = shop.images.all().order_by('-id')[:3]
    
    
    if request.method == 'POST':
        form = PersonUpdateForm(request.POST, request.FILES, instance=person)
        if request.user.id == person.username.id:
            add_image('shop_image_one', request, shop)
            add_image('shop_image_two', request, shop)
            add_image('shop_image_three', request, shop)

            update_shop(request, shop)

            if form.is_valid():
                form.save()
            return redirect('UserPage')
    context = {
        'user':user,
        'person':person,
        'form':form,
        'store':shop,
        'shop_images': shop_images
    }
    return render(request, 'user/user_home_page.html', context)




# Store
def store_view(request):
    return render(request, 'Store/store_page.html')
