from django.urls import path, re_path

from .import views

urlpatterns = [
    re_path(r'^(?P<when>[\w]+)$', views.index, name='event.index'),
    path('<slug>/', views.single, name='event.single')
]