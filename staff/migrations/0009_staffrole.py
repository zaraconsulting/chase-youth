# Generated by Django 3.2.5 on 2021-08-11 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0008_auto_20210806_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]