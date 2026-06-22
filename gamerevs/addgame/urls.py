from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'addgame'

urlpatterns = [
    path('', views.AddGameFormView.as_view(), name='addgame'),
    path('register/', views.AddUserFormView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='addgame/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('customize', views.customize_view, name='customize'),
]