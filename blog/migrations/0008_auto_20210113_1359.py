# Generated by Django 3.1 on 2021-01-13 07:59

import ckeditor_uploader.fields
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210111_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('keywords', multiselectfield.db.fields.MultiSelectField(choices=[('py', 'Python'), ('js', 'JavaScript'), ('css', 'CSS'), ('html', 'HTML'), ('dj', 'Django'), ('db', 'Database')], max_length=20)),
                ('author', models.CharField(default='http://sdt-inc.github.io/', max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('tag', multiselectfield.db.fields.MultiSelectField(choices=[('py', 'Python'), ('js', 'JavaScript'), ('css', 'CSS'), ('html', 'HTML'), ('dj', 'Django'), ('db', 'Database')], max_length=20)),
                ('writer_name', multiselectfield.db.fields.MultiSelectField(choices=[('NH', 'Md. Nahid Hassan'), ('MN', 'Md. Mehedi Hasan')], max_length=5)),
                ('date', models.DateField(auto_now=True)),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('related_page_link', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='pythondb',
            name='author',
            field=models.CharField(default='http://sdt-inc.github.io/', max_length=50),
        ),
    ]
