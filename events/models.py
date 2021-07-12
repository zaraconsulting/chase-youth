from django.db import models
from chase_youth.settings import env


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200, null=False)
    image = models.FileField(upload_to='events')
    excerpt = models.TextField(null=False)
    headline = models.TextField()
    is_complete = models.BooleanField(default=False)
    description_1 = models.TextField(null=False)
    description_2 = models.TextField(null=True, blank=True)
    description_3 = models.TextField(null=True, blank=True)
    description_4 = models.TextField(null=True, blank=True)
    description_5 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'image': self.image,
            'excerpt': self.excerpt,
            'headline': self.headline,
            'descriptions': [self.description_1, self.description_2, self.description_3, self.description_4, self.description_5],
            'date': {
                'date': self.date,
                'day': self.date.strftime('%d'),
                'month': self.date.strftime('%B'),
                'year': self.date.strftime('%Y'),
                'time': self.date.strftime('%I:%M'),
                'time_of_day': self.date.strftime('%p'),
            },
            'created_on': self.created_on,
        }
        return data

    def __str__(self):
        return f'{self.title} @{self.date}'

    def __repr__(self):
        return f'<Event: {self.title} @ {self.date}>'