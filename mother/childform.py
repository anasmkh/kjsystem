from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Child
from django.contrib.auth.models import User

class userCreation(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','username','password1', 'password2']


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = '__all__'

# class mealForm(forms.ModelForm):
#     class Meta:
#         model: Meal
#         fields = '__all__'
