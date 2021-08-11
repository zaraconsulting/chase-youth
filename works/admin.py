from django.contrib import admin
from .models import Work, TitleFontColor, TitleFontSize, ExcerptFontColor, ExcerptFontSize

class WorksAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'title_font_size', 'title_font_color', 'excerpt', 'excerpt_font_size', 'excerpt_font_color')

# Register your models here.
admin.site.register(Work, WorksAdmin)
admin.site.register(TitleFontSize)
admin.site.register(TitleFontColor)
admin.site.register(ExcerptFontSize)
admin.site.register(ExcerptFontColor)