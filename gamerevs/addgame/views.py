from django.http import request
from django.shortcuts import render, redirect
from django.views import generic
from .forms import GameForm, CustomizeForm
from gamereview.models import Game
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm
from django.contrib.auth import authenticate, login, mixins

# Create your views here.




class AddGameFormView(mixins.LoginRequiredMixin,generic.TemplateView):
    login_url = 'login/'
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

class AddUserFormView(generic.TemplateView):
    template_name = 'addgame/registrationform.html'

    #Display blank form
    def get(self, request):
        form = UserForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    #Process form data
    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            #return user object if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('gamereview:gamelist')

        return render(request, self.template_name, {'form': form})

def customize_view(request):
    context = {}

    if request.method == 'GET':
        context['form'] = CustomizeForm()
        print('current session is ', request.session.get('onoff','off'))
        return render(request, 'addgame/customize.html', context)

    if request.method == 'POST':
        form = CustomizeForm(request.POST)
        if form.is_valid():
            on_off_option = request.POST['on_off_field']
            request.session['onoff'] = on_off_option
        context['form'] = CustomizeForm()
        print('current session is ', request.session.get('onoff','off'))
        return render(request, 'addgame/customize.html', context)