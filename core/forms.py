from django.forms import ModelForm
from core.models import Person, Shop



class PersonUpdateForm(ModelForm):
    class Meta:
        model = Person
        fields = ['profile_picture', 'first_name', 'last_name', 'email', 'mobile', 'address']


class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = ['images', 'shop_name', 'address']


