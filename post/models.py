from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.

class UserPost(models.Model):
    """
    Stores a single user post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    approved = models.BooleanField(default=False)# Only True for fasting testing
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title} | by: {self.author}"

class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User`
    and :model:`post.UserPost`.
    """
    post = models.ForeignKey(
        UserPost, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.author}\n{self.body}"