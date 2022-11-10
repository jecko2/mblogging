from django.db import models
from organizer.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    comment=models.TextField()
    email = models.EmailField(max_length=100)
    is_public = models.BooleanField(default=False)
    
    
    class Meta:
        ordering = ['-pub_date']
        get_latest_by = "-pub_date"
    
    def __str__(self):
        return self.name

    
    
    

    
    