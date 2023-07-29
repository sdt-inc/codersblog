from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blog.models import PythonDB, BlogDB
from .serializers import PythonDBSerializer, BlogDBSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def python_db_list_create(request):
    if request.method == 'GET':
        python_dbs = PythonDB.objects.all()
        serializer = PythonDBSerializer(python_dbs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PythonDBSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def python_db_detail(request, pk):
    try:
        python_db = PythonDB.objects.get(pk=pk)
    except PythonDB.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = PythonDBSerializer(python_db)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PythonDBSerializer(python_db, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        python_db.delete()
        return Response(status=204)
    


@api_view(['GET', 'POST'])
def blog_db_list_create(request):
    pass

@api_view(['GET', 'PUT', 'DELETE'])
def blog_db_detail(request, pk):
    pass
