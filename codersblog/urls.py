from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf.urls import handler404

# 404 page handler config
# handler404 = "app_name.views.function_name"
handler404 = "blog.views.view_404"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
