from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='blog.index'),
    path('<slug>/', views.single, name='blog.single'),
    path('comment/news/<int:post_id>', views.comment, name='blog.comment'),
    path('tag/<tag_slug>', views.tags, name='blog.tags'),
]