from django.db import models

# Create your models here.
class Staff(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    image = models.FileField(upload_to='staff', null=True, blank=True)
    role = models.CharField(max_length=20)
    intro = models.TextField() 
    bio = models.TextField()

    def __repr__(self):
        return f'<Staff: {self.first_name} {self.last_name}>'