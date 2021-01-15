# from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from multiselectfield import MultiSelectField
from django.db.models.signals import pre_save
from .choice import keyword_choices, writer_choices
from codersblog.utils import unique_slug_generator


class PythonDB(models.Model):
    # all are <meta name='property' value>
    description = models.CharField(max_length=200)
    keywords = MultiSelectField(choices=keyword_choices, max_choices=3)
    author = models.CharField(
        max_length=50, default='http://sdt-inc.github.io/')

    # blog content
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    writer_name = MultiSelectField(
        choices=writer_choices, max_choices=3)

    date = models.DateField(auto_now=timezone.now())
    # body = RichTextField(config_name='special' blank=True, null=True)
    body = RichTextUploadingField(config_name='special', blank=True, null=True)
    related_page_link = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    # slug, sitemap
    def get_absolute_url(self):
        return reverse('tutorial', args=[str(self.id)])  # new


class BlogDB(models.Model):
    description = models.CharField(max_length=200)
    keywords = MultiSelectField(choices=keyword_choices, max_choices=3)
    author = models.CharField(
        max_length=50, default='http://sdt-inc.github.io/')

    # blog content
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True, blank=True)
    tag = MultiSelectField(choices=keyword_choices, max_choices=3)

    writer_name = MultiSelectField(
        choices=writer_choices, max_choices=1)

    date = models.DateField(auto_now=timezone.now())
    # body = RichTextField(config_name='special' blank=True, null=True)
    body = RichTextUploadingField(config_name='special', blank=True, null=True)
    related_page_link = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    # slug, sitemap
    def get_absolute_url(self):
        return reverse('blog_list', args=[str(self.id)])  # new


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


# everytime the PythonDB class object is created this below method is executed.
pre_save.connect(slug_generator, sender=PythonDB)
pre_save.connect(slug_generator, sender=BlogDB)


class UserEmail(models.Model):
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.email


class Comment(models.Model):
    blog = models.ForeignKey(BlogDB, on_delete=models.CASCADE)
    comment_body = RichTextField(config_name='special', blank=True, null=True)
