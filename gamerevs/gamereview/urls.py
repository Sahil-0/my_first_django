from .import views
from django.urls import path

app_name = 'gameReviewapp'

urlpatterns = [
    path('', views.GameListView.as_view(), name='gamelist'),
    path('<slug:slug>/', views.ReviewView.as_view(), name='review'),
    path('tags/', views.TagListView.as_view(), name='taglist'),
]