from django.forms import ModelForm
from gamereview.models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'