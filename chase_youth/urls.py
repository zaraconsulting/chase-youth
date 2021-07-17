"""chase_youth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .settings import env

from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='main.home'),
    path('contact/', views.contact, name='main.contact'),
    path('about-us/', views.about, name='main.about'),
    path('mailchimp/subscribe', views.mailchimp, name='main.mailchimp'),
    path('events/', include('events.urls')),
    path('staff/', include('staff.urls')),
    path('news/', include('blog.urls')),
    path('work/', include('works.urls'))
]

admin.site.site_header = f"{env('COMPANY_NAME')} CMS"
admin.site.site_title = f"{env('COMPANY_NAME')} CMS Portal"
admin.site.index_title = f"Welcome to the {env('COMPANY_NAME')} CMS Portal"