from django.forms import ModelForm
from gamereview.models import Game

class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'