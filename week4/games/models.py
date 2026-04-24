from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Tags(models.Model):
    label = models.CharField(max_length=20)

class Game(models.Model):
    title = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    platform = models.CharField(max_length=50, default='null')
    label_tag = models.ManyToManyField(Tags)
    slug = models.SlugField(max_length=150, default='null')

class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    review = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=150, default='null')
