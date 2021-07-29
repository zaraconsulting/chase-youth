from announcement.models import Announcement
from about.models import About
from django.shortcuts import render, redirect
from events.models import Event
from blog.models import Post
from works.models import Work
from django.core.mail import send_mail
from django.contrib import messages
from chase_youth.settings import env
from django.template.loader import render_to_string
from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

def home(request):
    context = {
        'event': Event.objects.order_by('-date').first() if Event.objects.all() else [],
        'events': Event.objects.order_by('-date').all() if Event.objects.all() else [],
        'news': Post.objects.order_by('-date_created').all()[:4],
        'works': Work.objects.all(),
        'announcement': Announcement.objects.first(),
    }
    return render(request, 'main/home.html', context)

def about(request):
    context = {
        'news': Post.objects.order_by('-date_created').all()[:4],
        'about': About.objects.all().first()
    }
    return render(request, 'main/about-us.html', context)

def contact(request):
    if request.method == 'POST':
        send_mail(
            subject='[ChaseYouth] Contact Form Inquiry',
            message=request.POST.get('message'),
            from_email=env('ADMIN_EMAIL_FROM'),
            recipient_list=[env('ADMIN_EMAIL_TO')],
            html_message=render_to_string(template_name='email/contact.html', context={ 'name': request.POST.get('contactName'), 'email': request.POST.get('email'), 'message': request.POST.get('message') })
        )
        messages.success(request, "Your email have been received! We will be in touch with you shortly.", extra_tags='green')
        return redirect('main.contact')
    
    context = {
        'event': Event.objects.order_by('-date').first()
    }
    return render(request, 'main/contact.html', context)

def mailchimp(request):
    if request.method == 'POST':
        mailchimp = Client()
        mailchimp.set_config({
            'api_key': settings.MAILCHIMP_API_KEY,
            'server': settings.MAILCHIMP_DATA_CENTER
        })

        member_info = {
            "email_address": request.POST.get('email'),
            "status": "subscribed",
        }

        try:
            response = mailchimp.lists.add_list_member(settings.MAILCHIMP_EMAIL_LIST_ID, member_info)
            # print("response: {}".format(response))
            messages.success(request, "You have signed up for our email list!", extra_tags='blue')
        except ApiClientError as error:
            messages.success(request, "There was an error. Please try again.", extra_tags='red')
            print("An exception occurred: {}".format(error.text))
        return redirect('main.home')