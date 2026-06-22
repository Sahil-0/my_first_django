from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Brand Table
class Brand(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    manufacturing_since = models.IntegerField()

    def __str__(self):
        return self.name


# Model Table
class PhoneModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=100)
    launch_date = models.DateField()
    platform = models.CharField(max_length=100)

    def __str__(self):
        return self.model_name


# Review Table
class Review(models.Model):
    models_reviewed = models.ManyToManyField(PhoneModel)
    review_text = models.TextField()
    date_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review_text[:50]

#new model added about news Link
class NewsLink(models.Model):
    model = models.ForeignKey(PhoneModel, on_delete=models.CASCADE)
    url = models.URLField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.user.username