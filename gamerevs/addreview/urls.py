from django.urls import path
from . import views

app_name = 'addreview'

urlpatterns = [
    path('', views.AddReviewFormView.as_view(), name='addreview'),
]