from django.shortcuts import render
from django.views.generic import ListView
from .models import Review, Game, Developer
from rest_framework import generics, viewsets
from .serializers import GameSerializer, DeveloperSerializer

# Create your views here.
class GameReviewListView(ListView):
    model = Review
    template_name = 'gamereview_list.html'
    context_object_name = 'reviews'

class GameApiView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def create(self, validated_data):
        return Game.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.developer = validated_data.get('developer', instance.developer)
        instance.platform = validated_data.get('platform', instance.platform)
        instance.save()
        return instance

class GameDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer