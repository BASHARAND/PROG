# Generated by Django 2.1.2 on 2018-12-10 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sel', '0003_auto_20181210_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Price',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
