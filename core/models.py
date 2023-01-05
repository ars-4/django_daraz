from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True


class Person(BaseModel):
    username=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    first_name=models.CharField(max_length=244, null=True)
    last_name=models.CharField(max_length=244, null=True)
    email=models.CharField(max_length=244, null=True)
    mobile=models.CharField(max_length=15, null=True)
    profile_picture=models.ImageField(upload_to='profiles', null=True)
    address=models.CharField(max_length=244, null=True)

    def __str__(self):
        return self.username.username


class Picture(BaseModel):
    title=models.CharField(max_length=244, null=True)
    image=models.ImageField(upload_to='uploads', null=True)

    def __str__(self):
        return self.title


class Shop(BaseModel):
    shop_name=models.CharField(max_length=244, null=True)
    images=models.ManyToManyField(Picture)
    owner=models.ForeignKey(Person, on_delete=models.CASCADE)
    address=models.CharField(max_length=244, null=True)

    def __str__(self):
        return self.shop_name


class Product(BaseModel):
    images=models.ForeignKey(Picture, on_delete=models.CASCADE)
    seller=models.ForeignKey(Shop, on_delete=models.CASCADE)
    title=models.CharField(max_length=244, null=True)
    price=models.CharField(max_length=244, null=True)
    stock=models.CharField(max_length=244, null=True)

    def __str__(self):
        return self.title


