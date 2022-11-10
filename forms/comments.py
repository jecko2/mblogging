from django import forms
from comment.models import Comment, CommentReply

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']
        
class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ['name', 'email', 'comment']