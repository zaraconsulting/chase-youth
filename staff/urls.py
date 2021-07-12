from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='staff.index'),
    path('member/<slug>', views.single, name='staff.single'),
]