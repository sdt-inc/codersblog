from django.urls import include, path, re_path

from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import PythonDB

from . import views


info_dict = {
    'queryset': PythonDB.objects.all(),
    'date_field': 'date',
}

urlpatterns = [
    path('', views.index, name='index'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('python/<int:pk>/', views.tutorial, name='tutorial'),
    re_path(r'search/\Z',
            views.search, name='search'),
    path('sitemap.xml', sitemap,
         {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6, changefreq='always')}},
         name='django.contrib.sitemaps.views.sitemap'),
]
