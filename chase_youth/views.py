from django.shortcuts import render, redirect
from events.models import Event
from blog.models import Post
from works.models import Work
from django.core.mail import send_mail
from chase_youth.settings import env
from django.template.loader import render_to_string

def home(request):
    context = {
        'event': Event.objects.order_by('-date').all()[0],
        'events': Event.objects.order_by('-date').all(),
        'news': Post.objects.order_by('-date_created').all()[:4],
        'works': Work.objects.all()
    }
    return render(request, 'main/home.html', context)

def contact(request):
    if request.method == 'POST':
        send_mail(
            subject='[ChaseYouth] Contact Form Inquiry',
            message=request.POST.get('message'),
            from_email=env('ADMIN_EMAIL_FROM'),
            recipient_list=[env('ADMIN_EMAIL_TO')],
            html_message=render_to_string(template_name='email/contact.html', context={ 'name': request.POST.get('contactName'), 'email': request.POST.get('email'), 'message': request.POST.get('message') })
        )
        return redirect('main.contact')
    context = {
        'event': Event.objects.order_by('-date').all()[0]
    }
    return render(request, 'main/contact.html', context)