from django.db import models
from profiles.models import UserProfile


APPROVAL = ((0, "Awaiting Moderation"), (1, "Approved"))
# Create your models here.


class BlogPost (models.Model):

    author = models.ForeignKey(UserProfile,
                               on_delete=models.SET_NULL)
    title = models.CharField(max_length=254, null=False, blank=False)
    blog_content = models.TextField(null=False, blank=False)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Blog Post: {self.title} Posted by: {self.author}'


class Comment (models.Model):

    commenter = models.ForeignKey(UserProfile,
                                  on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, null=False, blank=False)
    comment_content = models.TextField(null=False, blank=False)
    posted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    approved = models.IntegerField(choices=APPROVAL, default=0)

    def __str__(self):
        return f'Comment posted by: {self.commenter}'
