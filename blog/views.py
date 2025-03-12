from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Comment
from .forms import BlogForm, CommentForm

# Create your views here.


def blog(request):
    """ A view to show all blog posts"""

    blog_posts = BlogPost.objects.all()

    context = {
        'blog_posts': blog_posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_post(request, slug):
    """ A view to show individual blog posts """

    blog_post = get_object_or_404(BlogPost, slug=slug)

    context = {
        'blog_post': blog_post,
    }

    return render(request, 'products/product_detail.html', context)


# -------------------BLOG POST VIEWS-------------------
@login_required
def add_blog_post(request):
    """ Add a new blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add blog post. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog_post.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog_post(request, slug):
    """ Edit a blog post """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    blog_post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog_post)
        messages.info(request, f'You are editing {blog_post.title}')

    template = 'blog/edit_blog_post.html'
    context = {
        'form': form,
        'blog_post': blog_post,
    }

    return render(request, template, context)


@login_required
def delete_blog_post(request, slug):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that')
        return redirect(reverse('home'))

    """ Delete a product from the store """
    blog_post = get_object_or_404(BlogPost, slug=slug)
    blog_post.delete()
    messages.success(request, 'Blog Post deleted!')
    return redirect(reverse('blog'))


# -------------------COMMENT VIEWS-------------------
@login_required
def add_comment(request):
    """ Add a new comment """
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to add blog post. Please ensure the form is valid.')
    else:
        form = CommentForm()

    template = 'blog/add_comment.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_comment(request, slug, comment_id):
    """ Edit a blog post """
    blog_post = get_object_or_404(BlogPost, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.commenter == request.user:
        comment.save()
        messages.success(request, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only edit your own reviews!')

    template = 'blog/edit_comment.html'
    context = {
        'comment': comment,
        'blog_post': blog_post,
    }

    return render(request, template, context)


@login_required
def delete_comment(request, slug, comment_id):
    """ Delete a comment from a blog post """
    blog_post = get_object_or_404(BlogPost, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    if comment.commenter == request.user:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own reviews!')

    return redirect(reverse('product_detail', args=[blog_post.slug]))
