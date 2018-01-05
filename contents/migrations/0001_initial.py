# Generated by Django 2.0.1 on 2018-01-05 15:01

from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('page', models.CharField(choices=[('HO', 'Home'), ('AB', 'About'), ('TO', 'Town'), ('PR', 'Presell'), ('RE', 'Ready'), ('UP', 'Update'), ('CO', 'Contact')], default='HO', max_length=2)),
                ('content', tinymce.models.HTMLField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('geocode', location_field.models.plain.PlainLocationField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('completion_statis', models.CharField(choices=[('RE', 'Ready'), ('PRE', 'Pre-Selling')], default='RE', max_length=3)),
                ('completion_date', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='contents.Location')),
            ],
        ),
        migrations.CreateModel(
            name='UnitType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='unit_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='contents.UnitType'),
        ),
    ]