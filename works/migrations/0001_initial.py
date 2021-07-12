# Generated by Django 3.2.5 on 2021-07-12 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='works')),
                ('excerpt', models.TextField()),
                ('description_1', models.TextField()),
                ('description_2', models.TextField(blank=True, null=True)),
                ('description_3', models.TextField(blank=True, null=True)),
                ('description_4', models.TextField(blank=True, null=True)),
                ('description_5', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(default='', editable=False, max_length=200)),
            ],
        ),
    ]