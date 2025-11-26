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

    return render(
        request,
        "post/post_detail.html",
        {"userpost": post},
    )    