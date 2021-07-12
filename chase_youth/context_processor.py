from .settings import env
 
def export_context(request):
    data = {
        'COMPANY_NAME': env('COMPANY_NAME')
    }
    return data