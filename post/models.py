from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    img_tag = models.ImageField(upload_to="tags/",
                                default="img/post1.jpg"
                                )
    summary = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug":self.slug})
    
    # def get_create_url(self):
    #     return reverse("tag_create", kwargs={"slug": self.slug})


