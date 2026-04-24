from django.contrib import admin
from .models import Brand, PhoneModel, Review, NewsLink

# Register your models here.
admin.site.register(Brand)
admin.site.register(PhoneModel)
admin.site.register(Review)
admin.site.register(NewsLink)