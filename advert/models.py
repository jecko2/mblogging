from django.db import models

# Create your models here.


ADS_CATEGORY = (
    ("SPORTS", "Sports"),
    ("FINANCE", "Finance"),
    ("EDUCATION", "Education"),
    ("FIXED", "Fixed")
)

class AdvertImage(models.Model):
    add = models.ForeignKey("Advert", on_delete=models.CASCADE)
    img = models.ImageField(upload_to="adverts/", null=True, blank=True)

class Advert(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    img = models.ImageField(upload_to="adverts/", null=True, blank=True)
    link = models.URLField(max_length=255)
    is_public = models.BooleanField(default=False)
    category = models.CharField(max_length=100, choices=ADS_CATEGORY)
    is_active=models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.name}".lower()