from django.contrib import admin
from core.models import Person, Picture, Shop, Product

# Register your models here.

REGISTERED_MODELS = [
    Person,
    Picture,
    Shop,
    Product
]

admin.site.register(REGISTERED_MODELS)
