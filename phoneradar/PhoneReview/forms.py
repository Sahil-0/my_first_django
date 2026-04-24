from django.forms import ModelForm
from .models import PhoneModel, Review


class PhoneModelForm(ModelForm):
    class Meta:
        model = PhoneModel
        fields = '__all__'


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'