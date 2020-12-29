# from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from multiselectfield import MultiSelectField

from .choice import keyword_choices, writer_choices


class PythonDB(models.Model):
    # define your model here
    # all are <meta name='property' value>
    description = models.CharField(max_length=200)
    keywords = MultiSelectField(choices=keyword_choices, max_choices=3)
    author = models.CharField(
        max_length=399, default='http://sdt-inc.github.io/')

    # blog content
    title = models.CharField(max_length=200)
    writer_name = MultiSelectField(
        choices=writer_choices, max_choices=3)

    date = models.DateField(auto_now=timezone.now())
    # body = RichTextField(blank=True, null=True)
    body = RichTextUploadingField(config_name='default', blank=True, null=True)
    related_page_link = models.CharField(max_length=200)

    # slug
    # slug = models.SlugField()

    def __str__(self):
        return self.title

    # slug
    # def get_absolute_url(self):
    #     return reverse('blog_list', kwargs={'slug': self.slug})  # new
