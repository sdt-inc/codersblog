from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('python/<int:pk>/', views.tutorial, name='tutorial'),
    re_path(r'search/\Z',
            views.search, name='search')
]
