from django.db import models
from datetime import datetime as dt
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(default='', editable=False, max_length=200)

    class Meta:
        verbose_name_plural = 'Post Categories'
        
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}' 

class Post(models.Model):
    title = models.CharField(max_length=200)
    # image_display = models.FileField(upload_to='blog/post')
    is_featured = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    image = models.FileField(upload_to='blog/post')
    text1 = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    text5 = models.TextField(null=True, blank=True)
    text6 = models.TextField(null=True, blank=True)
    text7 = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', editable=False, max_length=200)


    def to_dict(self):
        data = {
            'id': self.id,
            'image': self.image,
            'title': self.title,
            'text1': self.text1,
            'text2': self.text2,
            'text3': self.text3,
            'text4': self.text4,
            'text5': self.text5,
            'text6': self.text6,
            'text7': self.text7,
            'text': [self.text1, self.text2, self.text3, self.text4, self.text5, self.text6, self.text7],
            'is_featured': self.is_featured,
            'date': {
                'timestamp': self.date_created,
                'display': dt.strftime(self.date_created, '%b %-d %Y, %-I:%-M %p')
            },
            'category': self.category,
            'slug': self.slug,
        }
        return data
        
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title.title()}' 


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    site = models.CharField(max_length=200, null=True)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Post Comments'

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'site': self.site,
            'text': self.text,
            'date': {
                'timestamp': self.date_created,
                'display': dt.strftime(self.date_created, '%-d %b %Y, %-I:%M %p')
            },
            'post': self.post.to_dict(),
        }
        return data

    def __str__(self):
        return f'{self.name} | {self.text[35:]}...' 


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default='', editable=False, max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Post Tags'
        
    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.slug}' 