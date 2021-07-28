from django.db import models
from datetime import datetime as dt
from django.utils.text import slugify

# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     email = models.CharField(max_length=200)
#     date_created = models.DateTimeField(max_length=200)

#     def __str__(self):
#         return f'[{self.email}] {self.first_name} {self.last_name}' 

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
    # email = models.CharField(max_length=200)
    image_display = models.FileField(upload_to='blog/post')
    image = models.FileField(upload_to='blog/post')
    text = models.TextField()
    is_featured = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE) 
    category = models.ForeignKey(Category , on_delete=models.CASCADE) 
    slug = models.SlugField(default='', editable=False, max_length=200)


    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            # 'email': self.email,
            'text': self.text,
            'date': {
                'timestamp': self.date_created,
                'display': dt.strftime(self.date_created, '%b %-d %Y, %-I:%-M %p')
            },
            # 'user': self.user,
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