from django.shortcuts import render
from .models import Staff

# Create your views here.
def index(request):
    context = {
        'staff': Staff.objects.all()
    }
    return render(request, 'staff/index.html', context)

def single(request):
    context = {}
    return render(request, 'staff/single.html', context)