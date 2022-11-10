from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from post.models import Tag
from account.models import User
from django.utils.text import slugify
import random
from django.db.models import Q



class PostQuerySet(models.QuerySet):
    def is_public(self, *args, **kwargs):
        return self.filter(public=True)
    
    def search(self,query, *args, **kwargs):
        lookup = Q(title__icontains=query)| Q(sub_title__icontains=query)|Q(content__icontains=query) | Q(sub_content__icontains=query)
        return self.is_public().filter(lookup)
    
class PostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return PostQuerySet(self.model, using=self._db)
    
    def search(self, query, *args, **kwargs):
        return self.get_queryset().is_public().search(query,  *args, **kwargs)
    
    

class Alert(models.Model):
    alert = models.CharField(max_length=100, unique=True)
    alert_content = models.CharField(max_length=300)
    
    def __str__(self):
        return self.alert
    
class PostImage(models.Model):
    name = models.CharField(max_length=100, unique=True)
    upload = models.ImageField(upload_to="post/", default='static/img/blog-thum1.jpg')
    source = models.URLField()
    
    def __str__(self):
        return self.name
    
GENRE_CHOICES = (
                ("FS", "Featured Stories"),
                ("DM", 'Drama'),
                ("DOC", "Documentary"),
            )

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    sub_title = models.CharField(max_length=100)
    content = models.TextField()
    sub_content = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    slug = models.SlugField(unique_for_month="pub_date")
    post_img = models.ImageField(upload_to="posts/", default="img/post1.jpg")
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True, blank=True)
    alert= models.ForeignKey(Alert, on_delete=models.SET_NULL, null=True, blank=True)
    sub_content_img= models.ForeignKey(PostImage, on_delete=models.SET_NULL, blank=True, null=True)
    quote = models.CharField(max_length=500)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES,default="FS")
    
    public = models.BooleanField(default=False)
    
    
    objects = PostManager()
    
    
    @property
    def random_time(self):
        return random.choice([random.randrange(4, 20)])
    
    class Meta:
        verbose_name = "post"
        verbose_name_plural = _("posts")
        ordering = ['-pub_date'] 
        get_latest_by = "-pub_date"
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={
            "year": self.pub_date.year,
            "month": self.pub_date.month,
            "day":self.pub_date.day,
            "slug":self.slug,
            })
        
    def get_home_url(self):
        return reverse("home")
        

class Comment(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    comment=models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    