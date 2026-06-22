from django.contrib import admin
from .models import Game, Tags, Review, Developer

# Register your models here.

admin.site.register(Game)
admin.site.register(Tags)
admin.site.register(Review)
admin.site.register(Developer)
