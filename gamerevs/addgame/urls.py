from . import views
from django.urls import path

app_name = 'addgame'

urlpatterns = [
    path('', views.AddGameFormView.as_view(), name='addgame'),
]