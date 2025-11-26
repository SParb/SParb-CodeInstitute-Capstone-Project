from django.shortcuts import render
from django.views import generic
from .models import UserPost
# Create your views here.

class PostList(generic.ListView):
    queryset = UserPost.objects.all()
    template_name = "userpost_list.html"