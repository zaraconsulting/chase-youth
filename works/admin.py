from django.contrib import admin
from .models import Work, WorkTitleFontColor, WorkTitleFontSize

class WorksAdmin(admin.ModelAdmin):
    fields = ('title', 'work_title_font_size', 'work_title_font_color')

# Register your models here.
admin.site.register(Work, WorksAdmin)
admin.site.register(WorkTitleFontSize)
admin.site.register(WorkTitleFontColor)