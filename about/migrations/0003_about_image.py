# Generated by Django 3.2.5 on 2021-08-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20210728_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='about_us'),
        ),
    ]
