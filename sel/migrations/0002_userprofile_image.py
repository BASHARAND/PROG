# Generated by Django 2.1.2 on 2018-11-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to=' Profile_image'),
        ),
    ]
