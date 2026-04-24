from django.contrib import admin

from .models import Game
from .models import Review
from .models import Tags

# Register your models here.

admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Tags)