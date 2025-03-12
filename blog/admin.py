from django.contrib import admin
from .models import BlogPost, Comment


# registering a class of BookAdmin
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.unregister(BlogPost)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment)
