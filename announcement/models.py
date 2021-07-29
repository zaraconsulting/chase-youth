from django.db import models

# Create your models here.
class Announcement(models.Model):
    header = models.CharField(max_length=100)
    input_text = models.CharField(max_length=100)
    button_text = models.CharField(max_length=50)
    description_line_1 = models.TextField()
    description_line_2 = models.TextField()

    def __str__(self):
        return self.header