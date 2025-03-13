from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.blog_post, name='blog_post'),
    path('edit/<slug:slug>/', views.edit_blog_post, name='edit_blog_post'),
]
