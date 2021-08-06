from events.models import Event
from .settings import env
 
def export_context(request):
    data = {
        'COMPANY_NAME': env('COMPANY_NAME'),
        'EVENTS': Event.objects.order_by('-created_on').all(),
        'ADMIN_EMAIL_TO': env('ADMIN_EMAIL_TO'),
        'FACEBOOK_URL': env('FACEBOOK_URL'),
        'ADMIN_PHONE': env('ADMIN_PHONE'),
    }
    return data