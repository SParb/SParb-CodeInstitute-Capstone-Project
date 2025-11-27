from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import UserPost
# Create your views here.

class PostList(generic.ListView):
    queryset = UserPost.objects.all()
    template_name = "post/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = UserPost.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    return render(
        request,
        "post/post_detail.html",
        {
            "userpost": post,
            "comments": comments,
            "comment_count": comment_count,
        },
    )    