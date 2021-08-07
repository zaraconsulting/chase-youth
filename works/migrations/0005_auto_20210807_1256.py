# Generated by Django 3.2.5 on 2021-08-07 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_auto_20210806_2050'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WorkTitleFontColor',
            new_name='TitleFontColor',
        ),
        migrations.RenameModel(
            old_name='WorkTitleFontSize',
            new_name='TitleFontSize',
        ),
        migrations.AlterModelOptions(
            name='titlefontcolor',
            options={'verbose_name_plural': 'Title Font Colors'},
        ),
        migrations.AlterModelOptions(
            name='titlefontsize',
            options={'verbose_name_plural': 'Title Font Sizes'},
        ),
        migrations.RenameField(
            model_name='work',
            old_name='work_title_font_color',
            new_name='title_font_color',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='work_title_font_size',
            new_name='title_font_size',
        ),
    ]
