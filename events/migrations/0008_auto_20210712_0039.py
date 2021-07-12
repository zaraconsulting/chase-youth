# Generated by Django 3.2.5 on 2021-07-12 00:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_event_is_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(),
        ),
    ]
