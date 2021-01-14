from django.urls import include, path, re_path
from django.conf.urls import url

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
    path('/<slug:slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('python/<slug:slug>/', views.tutorial, name='tutorial'),
    path('bloglist/', views.BlogListView.as_view(), name='blog_list'),
    re_path(r'search/\Z',
            views.search, name='search'),
    path('sitemap.xml', sitemap,
         {'sitemaps': {'blog': GenericSitemap(
             info_dict, priority=0.6, changefreq='hourly')}},
         name='django.contrib.sitemaps.views.sitemap'),
    path('editor', views.Editor, name='editor'),
    path('subscription', views.UserAdded, name='useradd'),
]
