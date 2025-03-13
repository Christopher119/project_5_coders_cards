from .models import BlogPost, Comment
from django import forms


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('author', 'title', 'blog_content')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_content',)
