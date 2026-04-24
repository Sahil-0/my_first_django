from django.http import request
from django.shortcuts import render
from django.views import generic
from .forms import GameForm
from gamereview.models import Game
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.




class AddGameFormView(generic.TemplateView):
    template_name = 'addgame/addgameform.html'


    def get(self, request):
        form = GameForm()
        games = Game.objects.all()
        args = {'form': form,
                'games': games}
        return render(request, self.template_name, args)

    def post(self, request):
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data['title']
            developer = form.cleaned_data['developer']
            platform = form.cleaned_data['platform']
            args = {'form': form,
                    'title': title,
                    'developer': developer,
                    'platform': platform}
            return HttpResponseRedirect(reverse('gamereview:gamelist'))

        games = Game.objects.all()
        return render(request, self.template_name, {'form': form, 'games': games})
