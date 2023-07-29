from rest_framework import serializers
from blog.models import PythonDB,BlogDB

class PythonDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = PythonDB
        fields = '__all__'

class BlogDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogDB
        fields = '__all__'
