# Generated by Django 4.2.3 on 2023-07-30 02:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_sponsordb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogdb',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='blogdb',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='blogdb',
            name='writer_name',
        ),
        migrations.RemoveField(
            model_name='pythondb',
            name='keywords',
        ),
        migrations.RemoveField(
            model_name='pythondb',
            name='writer_name',
        ),
    ]