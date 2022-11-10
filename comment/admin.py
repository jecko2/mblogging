from django.contrib import admin
from .models import Comment
# Register your models here.


def make_public(modelName, request, queryset):
    queryset.update(is_public=True)
    
make_public.shortdescription = "publish comment"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "is_public"]
    actions = (make_public, )
    
