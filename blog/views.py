from django.shortcuts import render
from .models import PythonDB


def index(request):
    data = PythonDB.objects.all()[1]
    context = {
        'description': str(data.description),
        'keywords': list(data.keywords),
        'author': str(data.author),
        'title': str(data.title),
        'writer_name': str(data.writer_name),
        'date': data.date,
        'body': data.body,
        'related_page_link': data.related_page_link,
    }
    return render(request, 'blog/index.html', context=context)


def tutorial(request):
    data = PythonDB.objects.all()[1]
    context = {
        'description': data.description,
        'keywords': list(data.keywords),
        'author': data.author,
        'title': data.title,
        'writer_name': data.writer_name,
        'date': data.date,
        'body': data.body,
        'related_page_link': data.related_page_link,
    }

    return render(request, 'blog/tutorial.html', context=context)
