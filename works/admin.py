from django.contrib import admin
from .models import Work, TitleFontColor, TitleFontSize, ExcerptFontColor, ExcerptFontSize

class WorksAdmin(admin.ModelAdmin):
    fields = ('title', 'image', 'title_font_size', 'title_font_color', 'excerpt', 'excerpt_font_size', 'excerpt_font_color', 'description_1', 'description_2', 'description_3', 'description_4', 'description_5')

# Register your models here.
admin.site.register(Work, WorksAdmin)
admin.site.register(TitleFontSize)
admin.site.register(TitleFontColor)
admin.site.register(ExcerptFontSize)
admin.site.register(ExcerptFontColor)