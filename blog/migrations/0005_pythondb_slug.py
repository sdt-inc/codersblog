# Generated by Django 3.1 on 2021-01-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201225_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='pythondb',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
