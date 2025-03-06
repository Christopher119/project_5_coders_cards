from django.contrib import admin
from .models import BlogPost, Comment


# registering a class of BookAdmin
@admin.register(BlogPost)
class BlogPostAdmin():

    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Comment)
