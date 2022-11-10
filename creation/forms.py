from django import forms
from post.models import Tag
from organizer.models import Post
from django.utils.text import slugify


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name", "img_tag","summary","content"]
        
    def save(self, commit):
        return super().save()

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
        "title","sub_title","content", "sub_content","post_img","tag","alert","sub_content_img","quote","genre",
        ]
        
    def save(self, commit):
        return super().save()