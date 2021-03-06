# Generated by Django 3.2.5 on 2021-07-10 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='media/')),
                ('excerpt', models.CharField(max_length=400)),
                ('headline', models.CharField(max_length=500)),
                ('description_1', models.TextField()),
                ('description_2', models.TextField()),
                ('description_3', models.TextField()),
                ('description_4', models.TextField()),
                ('description_5', models.TextField()),
                ('date', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
