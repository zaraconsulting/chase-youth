from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='staff.index'),
    path('member/', views.single, name='staff.single'),
]