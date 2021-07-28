from django.db import models

# Create your models here.
class About(models.Model):
    title1 = models.CharField(max_length=50)
    description1 = models.TextField()
    title2 = models.CharField(max_length=50)
    description2 = models.TextField()
    title3 = models.CharField(max_length=50)
    description3 = models.TextField()
    story_description1 = models.TextField()
    story_description2 = models.TextField()
    story_description3 = models.TextField()
    story_description4 = models.TextField()
    story_description5 = models.TextField()

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Manage About Page'
        

    def __str__(self):
        return f'{self.title1}: {self.description1}\n{self.title2}: {self.description2}\n{self.title3}: {self.description3}'