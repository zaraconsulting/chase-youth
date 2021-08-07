from django.contrib import admin

# from .models import User, Post, Category, Tag, Comment
from .models import Category, Post, Tag, Comment

class CategoryAdmin(admin.ModelAdmin):
    fields = ('name',)

class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'image', 'is_featured', 'text')

# Register your models here.
# admin.site.register(User)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)
admin.site.register(Comment)
