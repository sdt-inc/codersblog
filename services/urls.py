from django.urls import path
from . import views

urlpatterns = [
    path('api/coderblogs/python/', views.python_db_list_create, name='python-list-create'),
    path('api/coderblogs/python/<int:pk>/', views.python_db_detail, name='python-detail'),
    path('api/coderblogs/blog/', views.blog_db_list_create, name='blog-list-create'),
    path('api/coderblogs/blog/<int:pk>/', views.blog_db_detail, name='blog-detail'),
]
