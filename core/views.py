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
    shop = ''
    shop_images = ''
    products = ''
    if person.username.groups.all()[0].name == 'seller':
        shop = get_or_create_shop(person)
        products = Product.objects.filter(seller=shop)
        if shop.images:
            shop_images = shop.images.all().order_by('-id')[:3]

    context = {
        'person':person,
        'user': user,
        'store': shop,
        'shop_images': shop_images,
        'products': products
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
    shop = ''
    shop_images = ''
    products = ''
    if person.username.groups.all()[0].name == 'seller':
        shop = get_or_create_shop(person)
        products = Product.objects.filter(seller=shop)
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
        'shop_images': shop_images,
        'products': products
    }
    return render(request, 'user/user_home_page.html', context)




# Store
def store_view(request):
    return render(request, 'Store/store_page.html')




# Product
@login_required(login_url='LoginPage')
@multi_role(allowed_roles=['seller'])
def create_product(request):
    person = Person.objects.get(username=request.user)
    shop = Shop.objects.get(owner=person)
    allowed_products = [
        'cake', 'mousse', 'brownie', 'shake', 'coffee', 'cookie', 'ice', 'cream', 'chocolate'
    ]
    if request.method == 'POST':
        data = request.POST
        product_title = 'the_blank'
        product_title_lower = data['product_title'].lower()
        for item in allowed_products:
            if product_title_lower.__contains__(item):
                product_title = data['product_title']
        
        if product_title == 'the_blank':
            return redirect('CreateProductPage')
        else:
            picture = Picture.objects.create(
                title=product_title,
                image=request.FILES['product_image']
            )
            picture.save()
            product = Product.objects.create(
                seller=shop,
                title=product_title,
                price=data['product_price'],
                stock=data['product_stock'],
                tax=shop.tax,
                images = picture
            )
            product.save()
            return redirect('UserPage')
    context = {'allowed_products': allowed_products}
    return render(request, 'product/create.html', context)


@login_required(login_url='LoginPage')
def read_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {'product':product}
    return render(request, 'product/read.html', context)
