from django.shortcuts import render
from django.views import generic
from .models import Game, Tags


# Create your views here.
class GameListView(generic.ListView):
    template_name = 'gamereview/gamelist.html'
    context_object_name = 'all_games'

    def get_queryset(self):
        return Game.objects.all()


class ReviewView(generic.DetailView):
    model = Game
    template_name = 'gamereview/review.html'

class TagListView(generic.ListView):
    model = Tags
    template_name = 'gamereview/taglist.html'
    context_object_name = 'tags'

