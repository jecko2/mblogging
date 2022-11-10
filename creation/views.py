from django.shortcuts import render, redirect, get_object_or_404
from post.models import Tag
from organizer.models import Post
from .forms import TagForm, PostForm
from django.utils.text import slugify
from django import forms
from organizer.models import Post
from django.views.generic import View
from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from subscription.models import Subscription


class CreateTag(View):
    model = Tag
    form_class = TagForm
    template_name = "create_tag.html"

    
    def get(self, request, *args, **kwargs):
        context = {"form":self.form_class()}
        
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        data = self.form_class(request.POST, request.FILES)
        if data.is_valid():
            instance = data.save(commit=False)
            instance.slug = slugify(data.cleaned_data['name'])
            instance.save()
            return redirect("tag_list")
        context= {"form": data}
        return render(request, self.template_name, context)
    
    
    

class CreatePost(View):
    
    form_class = PostForm
    template_name = "create_post.html"
    subscribers = Subscription.objects.all()
    
    def get(self, request, *args, **kwargs):
        context = {"form":self.form_class()}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        data = self.form_class(request.POST, request.FILES)
        if data.is_valid():
            instance = data.save(commit=False)
            instance.author = request.user
            instance.slug = slugify(data.cleaned_data['title'])
            instance.save()
            
            # send_mail(
            # "NEW BLOG POST",
            # "Hello friend, this email is to inform you of the new blog post created. READ NOW here",
            # settings.EMAIL_HOST_USER,
            # [self.subscribers, ], 
            # )
            return redirect("tag_list")
        context= {"form": data}
        return render(request, self.template_name, context)
    



