# Generated by Django 2.1.2 on 2018-12-11 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sel', '0007_auto_20181211_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='get',
            name='Ch',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='get',
            name='K',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='get',
            name='M',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='get',
            name='Pot',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='get',
            name='Sh',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='get',
            name='T',
            field=models.BooleanField(default=True),
        ),
    ]
