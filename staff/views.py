from blog.models import Post
from django.shortcuts import get_object_or_404, render
from .models import Staff

# Create your views here.
def index(request):
    context = {
        'staff': Staff.objects.all()
    }
    return render(request, 'staff/index.html', context)

def single(request, slug):
    staff = get_object_or_404(Staff, slug=slug)
    context = {
        's': staff,
        'news': Post.objects.order_by('-date_created').all(),
    }
    return render(request, 'staff/single.html', context)