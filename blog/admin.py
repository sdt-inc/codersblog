from django.contrib import admin
from django.db.models import fields

from . import models
from .models import *


class PythonDBAdmin(admin.ModelAdmin):
    list_display = ('title','writer_name', 'date',)
    list_filter = ('date',)


# Customize Django Admin Panel
admin.site.site_header = 'DevCoders Admin Dashboard'
admin.site.site_title = 'DevCoders - SDT Inc'


admin.site.register(PythonDB, PythonDBAdmin)
admin.site.register(BlogDB)
admin.site.register(UserEmail)
admin.site.register(SponsorDB)
