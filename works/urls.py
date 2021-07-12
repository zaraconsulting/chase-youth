from django.urls import path, re_path

from .import views

urlpatterns = [
    path('<slug>/', views.single, name='works.single')
]