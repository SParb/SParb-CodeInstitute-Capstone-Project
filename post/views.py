from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import UserPost, Comment
from .forms import CommentForm, UserPostForm
# Create your views here.

class PostList(generic.ListView):
    """
    Returns all published posts in :model:`post.UserPost`
    and displays them in a page of six posts. 
    **Context**

    ``queryset``
        All published instances of :model:`post.UserPost`
    ``paginate_by``
        Number of posts per page.
        
    **Template:**

    :template:`post/index.html`
    """
    queryset = UserPost.objects.all()
    template_name = "post/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`post.UserPost`.

    **Context**

    ``post``
        An instance of :model:`post.UserPost`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`post.CommentForm`

    **Template:**

    :template:`post/post_detail.html`
    """

    queryset = UserPost.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval')

    comment_form = CommentForm()

    return render(
        request,
        "post/post_detail.html",
        {
            "userpost": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )    
def create_post(request):
    if request.method == 'POST':
        create_post_form = UserPostForm(request.POST)
        if create_post_form.is_valid():
            post = create_post_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(
            request, messages.SUCCESS,
            'Comment submitted and awaiting approval')
            return redirect('home')  # Change to your posts list view
        
    create_post_form= UserPostForm()
    return render(request, 'post/create_post.html', {'form': create_post_form})

def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`post.UserPost`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`post.CommentForm`
    """
    if request.method == "POST":

        queryset = UserPost.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`post.UserPost`.
    ``comment``
        A single comment related to the post.
    """
    queryset = UserPost.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))