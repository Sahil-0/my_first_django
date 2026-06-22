from django.forms import ModelForm
from .models import PhoneModel, Review
from django.contrib.auth.models import User
from django import forms


class PhoneModelForm(ModelForm):
    class Meta:
        model = PhoneModel
        fields = '__all__'


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']