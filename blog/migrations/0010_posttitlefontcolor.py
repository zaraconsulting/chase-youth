# Generated by Django 3.2.5 on 2021-08-06 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210806_1923'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTitleFontColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Post Title Font Colors',
            },
        ),
    ]