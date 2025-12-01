from .models import Comment, UserPost
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ['title', 'pet_type', 'featured_image', 'content']