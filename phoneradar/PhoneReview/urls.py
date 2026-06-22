from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brand/<int:brand_id>/', views.brand_models, name='brand_models'),
    path('model/<int:model_id>/', views.model_detail, name='model_detail'),
    path('add-phone/', views.add_phone, name='add_phone'),
    path('add-review/', views.add_review, name='add_review'),
    path('register/', views.AddUserFormView.as_view(), name='register'),
]