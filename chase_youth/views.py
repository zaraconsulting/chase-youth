from django.shortcuts import render
from events.models import Event
from blog.models import Post

def home(request):
    context = {
        'event': Event.objects.order_by('-date').all()[0],
        'events': Event.objects.order_by('-date').all(),
        'news': Post.objects.order_by('-date_created').all()[:4]
    }
    return render(request, 'main/home.html', context)

def contact(request):
    context = {
        'event': Event.objects.order_by('-date').all()[0]
    }
    return render(request, 'main/contact.html', context)