# Generated by Django 3.1 on 2020-12-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pythondb',
            name='related_page_link',
            field=models.CharField(max_length=200),
        ),
    ]
