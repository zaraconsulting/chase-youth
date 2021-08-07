from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from .models import Event
from datetime import datetime as dt
from django.core.paginator import Paginator

# Create your views here.
def index(request, when=None):
    if when == 'upcoming':
        events = [i for i in Event.objects.order_by('-created_on').all() if not i.is_complete]
    elif when == 'past':
        events = [i for i in Event.objects.order_by('-created_on').all() if i.is_complete]
    elif when == 'all':
        events = [i for i in Event.objects.order_by('-created_on').all()]
    context = {
        'events': events,
        # 'events': Paginator(events, 5).object_list,
        'sidebar_events': [i for i in Event.objects.order_by('-created_on').all()][:5]
    }
    return render(request, 'events/index.html', context)

def single(request, event_id):
    e = get_object_or_404(Event, id=event_id)
    context = {
        'e': e.to_dict(),
        'upcoming_events': [i for i in Event.objects.order_by('date').all() if not i.is_complete][:5],
        'referrer': 'event.index'
    }
    return render(request, 'events/single.html', context)