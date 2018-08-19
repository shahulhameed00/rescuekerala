# Generated by Django 2.1 on 2018-08-19 04:20

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0052_auto_20180819_0128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='image',
            field=models.ImageField(blank=True, upload_to=mainapp.models.upload_to),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='upload',
            field=models.FileField(blank=True, upload_to=mainapp.models.upload_to),
        ),
    ]