from django.db import models

# Create your models here.
class About(models.Model):
    image = models.FileField(upload_to='about_us', null=True, blank=True)
    title1 = models.CharField(max_length=50)
    description1 = models.TextField()
    title2 = models.CharField(max_length=50)
    description2 = models.TextField()
    title3 = models.CharField(max_length=50)
    description3 = models.TextField()
    story_description1 = models.TextField()
    story_description2 = models.TextField(null=True, blank=True)
    story_description3 = models.TextField(null=True, blank=True)
    story_description4 = models.TextField(null=True, blank=True)
    story_description5 = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Manage About Page'
        

    def __str__(self):
        return "Click here to manage the content on the 'About Us' page"