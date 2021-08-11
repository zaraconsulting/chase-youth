from blog.models import Post
from django.shortcuts import get_object_or_404, render
from .models import Staff
from django.http import request

# Create your views here.
def index(request):
    context = {
        'staff': Staff.objects.order_by('staff_role__rank').all(),
    }
    return render(request, 'staff/index.html', context)

def single(request, slug):
    staff = get_object_or_404(Staff, slug=slug)
    context = {
        's': staff,
        'news': Post.objects.order_by('-date_created').all(),
        'referrer': 'staff.index',
    }
    return render(request, 'staff/single.html', context)