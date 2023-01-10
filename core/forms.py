from django.forms import ModelForm
from core.models import Person



class PersonUpdateForm(ModelForm):
    class Meta:
        model = Person
        fields = ['profile_picture', 'first_name', 'last_name', 'email', 'mobile', 'address']

