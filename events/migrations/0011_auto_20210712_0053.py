# Generated by Django 3.2.5 on 2021-07-12 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20210712_0042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
