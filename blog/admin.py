from django.contrib import admin
from django.db.models import fields

from . import models
from .models import *

# Register your models here.
# class PythonDB(models.Model):
#     class Meta:
#         fields = '__all__'

admin.site.register(PythonDB)
admin.site.register(BlogDB)
admin.site.register(UserEmail)