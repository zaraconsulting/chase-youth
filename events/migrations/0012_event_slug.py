# Generated by Django 3.2.5 on 2021-08-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20210712_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=200),
        ),
    ]
