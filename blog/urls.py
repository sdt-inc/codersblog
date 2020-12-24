from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.BlogListView.as_view(), name='blog_list'),
    path('', views.index, name='index'),
    path('python/<int:pk>', views.tutorial, name='tutorial'),
]
