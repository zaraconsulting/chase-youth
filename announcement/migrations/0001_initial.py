# Generated by Django 3.2.5 on 2021-07-29 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100)),
                ('input_text', models.CharField(max_length=100)),
                ('button_text', models.CharField(max_length=50)),
                ('description_text', models.TextField()),
            ],
        ),
    ]
