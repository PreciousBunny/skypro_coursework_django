from django.contrib.auth.decorators import login_required
from django.urls import path, re_path
from blog.apps import BlogConfig
from .views import *


app_name = BlogConfig.name


urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('blog/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('create', PostCreateView.as_view(), name='post_create'),
    path('update/<slug:slug>', PostUpdateView.as_view(), name='post_update'),
    path('delete/<slug:slug>', PostDeleteView.as_view(), name='post_delete'),
    path('toggle/<slug:slug>', login_required(toggle_publish), name='toggle_publish'),
    path('allposts', PostAllListView.as_view(), name='all_posts'),
]
