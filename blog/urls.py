from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('ckeditor/', include(
        'ckeditor_uploader.urls')),
    path('python/<int:pk>/', views.tutorial, name='tutorial'),
]

# for serving ckeditor js files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, settings.STATIC_ROOT)
