# Generated by Django 3.2.5 on 2021-08-06 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0006_auto_20210806_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]