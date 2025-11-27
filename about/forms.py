from .models import FeedbackRequest
from django import forms


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackRequest
        fields = ('name', 'email', 'message')