# Generated by Django 3.2.5 on 2021-07-28 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_is_featured'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Post Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'Post Comments'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': 'Post Tags'},
        ),
    ]