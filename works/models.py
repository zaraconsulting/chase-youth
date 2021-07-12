from django.db import models
from django.utils.text import slugify

# Create your models here.
class Work(models.Model):
    title = models.CharField(max_length=200, null=False)
    image = models.FileField(upload_to='works')
    excerpt = models.TextField(null=False)
    description_1 = models.TextField(null=False)
    description_2 = models.TextField(null=True, blank=True)
    description_3 = models.TextField(null=True, blank=True)
    description_4 = models.TextField(null=True, blank=True)
    description_5 = models.TextField(null=True, blank=True)
    slug = models.SlugField(default='', editable=False, max_length=200)

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'image': self.image,
            'excerpt': self.excerpt,
            'descriptions': [self.description_1, self.description_2, self.description_3, self.description_4, self.description_5],
        }
        return data

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'<Work: {self.title}>'