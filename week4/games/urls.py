from django.urls import path, include
from .views import GameApiView, GameDetailApiView, GameReviewListView
from rest_framework.routers import DefaultRouter
from .views import DeveloperViewSet

router = DefaultRouter()
router.register('developers', DeveloperViewSet)

urlpatterns = [
    path('reviews/', GameReviewListView.as_view(), name='review-list'),
    path('gameapi/', GameApiView.as_view()),
    path('gameapi/<int:pk>/', GameDetailApiView.as_view()),
    path("", include(router.urls)),
]