from django.conf import settings
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from blog import views

# 404 page handler config
# handler404 = "app_name.views.function_name"
handler404 = "blog.views.view_404"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('service/',include('services.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# for serving ckeditor js files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
