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
    queryset = UserPost.objects.filter(approved=True)
    template_name = "post/index.html"
    paginate_by = 6

    def get_queryset(self):
        """
        Returns a filtered queryset of :model:`post.UserPost`
        based on GET parameters.

        **Context**

        ``queryset``
            All published instances of :model:`post.UserPost`,
            filtered by pet type and/or author.
        ``pet_type``
            The pet type to filter posts by,
            from GET parameter `filterByPetType`.
        ``user_filter``
            The user filter to show only the current user's posts,
            from GET parameter `filterByUser`.

        **Returns:**
            Queryset of filtered :model:`post.UserPost` objects.
        """
        queryset = super().get_queryset()
        pet_type = self.request.GET.get('filterByPetType')
        user_filter = self.request.GET.get('filterByUser')
        if pet_type and pet_type != 'all':
            queryset = queryset.filter(pet_type__iexact=pet_type)
        if user_filter == 'myPosts' and self.request.user.is_authenticated:
            queryset = queryset.filter(author=self.request.user)
        return queryset

    def get_context_data(self, **kwargs):
        """
        Adds extra context (comment count) to the
        template for :model:`post.UserPost` list view.

        """
        context = super().get_context_data(**kwargs)
        for post in context['object_list']:
            post.comment_count = post.comments.filter(approved=True).count()
        context['current_pet_type'] = self.request.GET.get(
            'filterByPetType', 'all')
        context['current_user_filter'] = self.request.GET.get(
            'filterByUser', 'all')
        return context


def post_detail(request, post_id):
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

    :template:`post_detail.html`
    """

    try:
        post = UserPost.objects.get(id=post_id)
        comments = post.comments.all().order_by("-created_on")
        comment_count = post.comments.filter(approved=True).count()
        comment_form = CommentForm()
        # ...any other logic for existing posts...
    except UserPost.DoesNotExist:
        post = None
        comments = []
        comment_count = 0
        comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval.')

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


def post_create(request):
    """
    Create an instance of :model:`post.UserPost`.

    **Context**

    ``post``
        An instance of :model:`post.UserPost`.
    ``post_create_form``
        An instance of :form:`post.UserPostForm`

    **Template:**

    :template:`post_create.html`
    """
    if request.method == 'POST':
        post_create_form = UserPostForm(request.POST, request.FILES)
        if post_create_form.is_valid():
            post = post_create_form.save(commit=False)
            post.author = request.user
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post submitted and awaiting approval.')
            return redirect('home')  # Change to your posts list view

    post_create_form = UserPostForm()
    return render(
        request, 'post/post_create.html',
        {'post_create_form': post_create_form, },)


def comment_edit(request, post_id, comment_id):
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
        post = get_object_or_404(queryset, id=post_id)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment updated and awaiting approval.')
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error updating comment.')

    return HttpResponseRedirect(reverse('post_detail', args=[post_id]))


def comment_delete(request, post_id, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`post.UserPost`.
    ``comment``
        A single comment related to the post.
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted.')
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own comments.')

    return HttpResponseRedirect(reverse('post_detail', args=[post_id]))


def post_edit(request, post_id):
    """
    Edit a post.

    **Context**

    ``post``
        An instance of :model:`post.UserPost`.

    ``post_edit_form``
        An instance of :form:`post.UserPostForm`

    **Template:**

    :template:`post_edit.html`
    """
    post = get_object_or_404(UserPost, id=post_id)
    if request.method == 'POST':
        post_edit_form = UserPostForm(
            request.POST, request.FILES, instance=post)
        if post_edit_form.is_valid():
            post = post_edit_form.save(commit=False)
            post.approved = False
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post updated and awaiting approval.')
            return redirect('home')
    else:
        post_edit_form = UserPostForm(instance=post)
    return render(request, 'post/post_edit.html', {
        'post_edit_form': post_edit_form,
        'userpost': post,
    })


def post_delete(request, post_id):
    """
    Delete a post.

    **Context**

    ``post``
        An instance of :model:`post.UserPost`.
    """
    post = get_object_or_404(UserPost, id=post_id)
    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted.')

    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own posts.')
    return redirect('home')
