from django.contrib import admin
from .models import BlogPost, Comment


# registering a class of BlogAdmin
class BlogPostAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = (
        'author',
        'title',
        'posted',
        'updated',
    )
    ordering = ('posted',)


class CommentAdmin(admin.ModelAdmin):

    list_display = (
        'commenter',
        'blog_post',
        'approved',
    )


# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
