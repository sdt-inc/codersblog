# Generated by Django 3.1.4 on 2021-01-16 19:56

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20210116_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdb',
            name='keywords',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('JavaScript', 'JavaScript'), ('CSS', 'CSS'), ('HTML', 'HTML'), ('Django', 'Django'), ('PHP', 'PHP'), ('Others', 'Others')], max_length=44),
        ),
        migrations.AlterField(
            model_name='blogdb',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='blogdb',
            name='tag',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('JavaScript', 'JavaScript'), ('CSS', 'CSS'), ('HTML', 'HTML'), ('Django', 'Django'), ('PHP', 'PHP'), ('Others', 'Others')], max_length=44),
        ),
        migrations.AlterField(
            model_name='blogdb',
            name='writer_name',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('NH', 'Md. Nahid Hassan'), ('MN', 'Md. Mehedi Hasan'), ('M3C', 'Mursalin Chowdhury')], max_length=9),
        ),
        migrations.AlterField(
            model_name='pythondb',
            name='keywords',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Python', 'Python'), ('JavaScript', 'JavaScript'), ('CSS', 'CSS'), ('HTML', 'HTML'), ('Django', 'Django'), ('PHP', 'PHP'), ('Others', 'Others')], max_length=44),
        ),
        migrations.AlterField(
            model_name='pythondb',
            name='writer_name',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('NH', 'Md. Nahid Hassan'), ('MN', 'Md. Mehedi Hasan'), ('M3C', 'Mursalin Chowdhury')], max_length=9),
        ),
    ]
