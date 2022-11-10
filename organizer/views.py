from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse
from .models import Post
from post.models import Tag
from django.shortcuts import get_object_or_404
from subscription.models import Subscription
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from comment.models import Comment
from forms.comments.forms import CommentForm
from django.contrib import messages
from advert.models import Advert

from django.core.mail import send_mail
from django.conf import settings


class SubscriptionViewMixin:
    success_url = ""
    instance = None
    def post(self, request, year=None, month=None, day=None, slug=None, *args, **kwargs):
        
        if "subscribeForm" in request.POST:
                instance = request.POST.get("email", None)
                if instance is not None:
                    store = Subscription.objects.filter(email=instance)
                    if store.exists():
                        messages.warning(request, "You're already subscribed")
                    else:
                        Subscription.objects.create(email=instance)
                        messages.success(request, "Subscription successful")
                        # send_mail(
                        #     'SUBSCRIPTION SUCCESS',
                        #     'Hello {instance}, your subscription was successfull.',
                        #     settings.EMAIL_HOST_USER,
                        #     [instance, ],
                        #     fail_silently=False,
                        # )
                        return redirect(self.success_url)
        return redirect(self.success_url)
    
 


class ViewHome(generic.View, SubscriptionViewMixin):
    
    template_name = "index.html"
    model = Post
    form_class = None
    paginate_by = 3
    page_kwarg = "page"
    success_url = "home"
    
    
    def get(self, request, *args, **kwargs):
        paginator = Paginator(self.model.objects.filter(public=True).all(), self.paginate_by)
        page_num = request.GET.get(self.page_kwarg)
        add = Advert.objects.filter(is_public=True).all()
        
        
        try:
            page = paginator.page(page_num)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        
        if page.has_previous():
            prev_url = "?{kwarg}={n}".format(kwarg=self.page_kwarg, n=page.previous_page_number())
        else: prev_url = None
             
        if page.has_next():
            next_url = "?{kwarg}={n}".format(kwarg=self.page_kwarg, n=page.next_page_number())
        else: next_url=None
            
        context = {
            "posts": page,
            "paginator":paginator,
            "is_paginated": page.has_other_pages(),
            "prev_url": prev_url,
            "next_url": next_url,
            "tags": Tag.objects.all()[:5],
            "adverts":add,
        
        }
        
        return render(request, self.template_name, context)
    
    

class PostDetailView(generic.View, SubscriptionViewMixin):
    template_name = "single-blog.html"
    model = Post
    success_url = "home"
    comment_form = CommentForm
    page_kwargs = "page"
    paginate_comment_by = 3
    
    def get(self, request, year, month, day, slug, *args, **kwargs):
        
        post = get_object_or_404(self.model, pub_date__year=year, pub_date__month=month,
                                 pub_date__day=day, slug__iexact=slug)
        comment_paginator = Paginator(Comment.objects.filter(is_public=True, post=post).all(), self.paginate_comment_by)
        page_num = request.GET.get(self.page_kwargs)
        try:
            comm_page = comment_paginator.page(page_num)
        except PageNotAnInteger:
            comm_page = comment_paginator.page(1)
        except EmptyPage:
            comm_page = comment_paginator.page(comment_paginator.num_pages)
            
        if comm_page.has_previous():
            prev_com_url = "?{kwargs}={n}".format(kwargs=self.page_kwargs, n=comm_page.previous_page_number())
        else: prev_com_url = None
        if comm_page.has_next():
            next_com_url = "?{kwargs}={n}".format(kwargs=self.page_kwargs, n=comm_page.next_page_number())
        else:next_com_url = None
            
            
        context = {
            "is_comment_paginated":comm_page.has_other_pages(),
            "post": post,
            'comment_pages':comment_paginator,
            "prev_com_url":prev_com_url,
            "next_com_url": next_com_url,
            "comments":comm_page,
            "comment_form": self.comment_form(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request, year, month, day, slug, pk=None, *args, **kwargs):
        
        post = get_object_or_404(self.model, pub_date__year=year, pub_date__month=month,
                                 pub_date__day=day, slug__iexact=slug)
        
        
        if "commentForm" in request.POST:
            comment_form = self.comment_form(request.POST)
            print(comment_form)
            if comment_form.is_valid():
                form = comment_form.save(commit=False)
                form.post = post
                form.save()
                messages.success(request, "Your comment was posted succesfully awaiting moderation")
                return redirect(post)
                
        return redirect(post)



class TagHomeView(generic.View, SubscriptionViewMixin):
    
    template_name = "tag-page.html"
    model = Tag
    paginate_by = 3
    page_kwarg = "page"
    success_url = "home"
    
    def get(self, request, *args, **kwargs):
        paginator = Paginator(self.model.objects.all(), self.paginate_by)
        page_num = request.GET.get(self.page_kwarg)
        add = Advert.objects.filter(is_public=True).all()
        
        
        try:
            page = paginator.page(page_num)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
            
        if page.has_previous():
            prev_url = "?{kwarg}={n}".format(kwarg=self.page_kwarg, n=page.previous_page_number())
        else: prev_url = None
        
        if page.has_next():
            next_url = "?{kwarg}={n}".format(kwarg=self.page_kwarg, n=page.next_page_number()) 
        else: next_url = None          
        
        context = {
            "is_paginated": page.has_other_pages(),
            "tag_list": page,
            "prev_url": prev_url,
            "next_url":next_url,
            "pages": paginator.num_pages,
            "adverts":add,
        }
        return render(request, self.template_name, context)



    
class TagDetailView(generic.View, SubscriptionViewMixin):
    template_name = "single-tag.html"
    model = Tag
    success_url = "home"
    paginate_posts_by = 3
    page_kwargs = "page"
    
    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(self.model, slug__iexact=slug)
        post_paginator = Paginator(Post.objects.filter(tag=tag, public=True).all(), self.paginate_posts_by)
        page_num = request.GET.get(self.page_kwargs)
        add = Advert.objects.filter(is_public=True).all()
        try:
            post_page = post_paginator.page(page_num)
        except PageNotAnInteger:
            post_page = post_paginator.page(1)
        except EmptyPage:
            post_page = post_paginator.page(post_paginator.num_pages)
            
        if post_page.has_previous():
            prev_url = "?{kwargs}={n}".format(kwargs=self.page_kwargs, n=post_page.previous_page_number())
        else: prev_url = None  
        
        if post_page.has_next():
            next_url = "?{kwargs}={n}".format(kwargs=self.page_kwargs, n=post_page.next_page_number())
        else: next_url = None 
                     
        context = {
            "tag": tag,
            "related_posts": post_page,
            "is_paginated":post_page.has_other_pages(),
            "prev_url":prev_url,
            "next_url":next_url,
            "adverts":add,
            "paginator":post_paginator
            
        }
        return render(request, self.template_name, context)



