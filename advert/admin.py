from django.contrib import admin
from .models import Advert, AdvertImage
# Register your models here.

@admin.register(Advert)
class AdminAdvert(admin.ModelAdmin):
    list_display = ['name', 'link', 'is_public', 'category']
    

@admin.register(AdvertImage)
class AdminAdvert(admin.ModelAdmin):
    
    list_display = ['add', 'img']