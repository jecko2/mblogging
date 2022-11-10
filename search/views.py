from django.shortcuts import render
from django.views.generic import View
from post.models import Tag
from organizer.models import Post
from django.http import HttpResponse


class SearchBlogView(View):
    model = Post
    
    def get(self, request, *args, **kwargs):
        q = self.model.objects.get_queryset(*args, **kwargs)
        query = request.GET.get("search", None)
        context = {}
        pass
    
    

        
