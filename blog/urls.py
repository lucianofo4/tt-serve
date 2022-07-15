from django.contrib import admin
from django.urls import path
from . import views as blog_views
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.auth import views as auth_views

# app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('post/new/', PostCreateView.as_view(), name="post_create"),
    path('todo/', blog_views.todo_list, name="todo_list"),
    path('deu/', blog_views.deu, name='deu'),
    path('jaime/', blog_views.jaime, name='jaime'),
    path('pequenodiu/', blog_views.pequenodiu, name='pequenodiu'),

]
