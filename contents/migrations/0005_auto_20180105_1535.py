# Generated by Django 2.0.1 on 2018-01-05 15:35

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_auto_20180105_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='geocode',
            field=location_field.models.plain.PlainLocationField(max_length=63),
        ),
    ]
