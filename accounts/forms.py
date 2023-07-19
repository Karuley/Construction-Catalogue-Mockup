from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ('name', 'image', 'price', 'category', 'tags', 'description',)

class EditCompany(ModelForm):
    class Meta:
        model = Company
        fields = ('logo', 'name', 'email', 'phone', 'adress')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

"""class LoginUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password']"""