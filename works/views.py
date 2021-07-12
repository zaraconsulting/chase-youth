from blog.models import Post
from django.shortcuts import get_object_or_404, render
from .models import Work

# Create your views here.
def single(request, slug):
    w = get_object_or_404(Work, slug=slug)
    context = {
        'w': w.to_dict(),
        'news': Post.objects.order_by('-date_created').all()
    }
    return render(request, 'works/single.html', context)