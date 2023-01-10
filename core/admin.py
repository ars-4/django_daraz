from django.contrib import admin
from core.models import Person, Order, Picture, Shop, Product

# Register your models here.

REGISTERED_MODELS = [
    Person,
    Picture,
    Shop,
    Product,
    Order
]

admin.site.register(REGISTERED_MODELS)
