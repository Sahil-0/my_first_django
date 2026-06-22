from django.forms import ModelForm
from gamereview.models import Game
from django.contrib.auth.models import User
from django import forms

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

class UserForm(ModelForm):
    email = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        data = self.cleaned_data['email']

        if "@gmail.com" not in data:
            raise forms.ValidationError("Must be a gmail address")

        return data

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

ON_OFF = [
    ('on', 'ON'),
    ('off', 'OFF'),
]

#creating a form
class CustomizeForm(forms.Form):
    on_off_field = forms.CharField(label='On or Off?', widget=forms.Select(choices=ON_OFF))