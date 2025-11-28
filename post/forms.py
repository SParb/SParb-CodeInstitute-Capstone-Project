from .models import Comment, UserPost
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ['title', 'slug', 'featured_image', 'content']