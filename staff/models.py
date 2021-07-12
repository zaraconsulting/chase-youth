from django.db import models
from django.utils.text import slugify

# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    image = models.FileField(upload_to='staff', null=True, blank=True)
    role = models.CharField(max_length=50, null=True, blank=True)
    intro = models.TextField() 
    bio = models.TextField()
    slug = models.SlugField(default='', editable=False, max_length=200)

    def save(self, *args, **kwargs):
        value = f'{self.first_name} {self.last_name}'.replace(' ', '-').lower()
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __repr__(self):
        return f'<Staff: {self.first_name} {self.last_name}>'