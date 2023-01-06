# Generated by Django 4.1.4 on 2022-12-26 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_dynamicmix_separator_alter_staticmix_separator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamicmix',
            name='bitrate',
            field=models.IntegerField(choices=[(0, 'WAV'), (1, 'FLAC'), (192, '192 kbps'), (256, '256 kbps'), (320, '320 kbps')], default=256),
        ),
        migrations.AlterField(
            model_name='staticmix',
            name='bitrate',
            field=models.IntegerField(choices=[(0, 'WAV'), (1, 'FLAC'), (192, '192 kbps'), (256, '256 kbps'), (320, '320 kbps')], default=256),
        ),
    ]