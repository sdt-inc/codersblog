from django.shortcuts import render, get_object_or_404
from .models import PythonDB
from django.views.generic import ListView
from django.urls import resolve


def index(request):
    # current_url = resolve(request.path_info).url_name
    # test_data = PythonDB.objects.values_list('title')
    # print(test_data)

    data = PythonDB.objects.all()[2]
    context = {
        'description': str(data.description),
        'keywords': list(data.keywords),
        'author': str(data.author),
        'title': str(data.title),
        'writer_name': str(data.writer_name),
        'date': data.date,
        'body': data.body,
        'related_page_link': data.related_page_link,
        # 'test_data': test_data,
    }
    return render(request, 'blog/index.html', context=context)


def tutorial(request, pk=None):
    # data = PythonDB.objects.get(pk=pk)
    data = get_object_or_404(PythonDB, pk=pk)

    # get current url path name
    current_url = resolve(request.path_info).url_name

    # return all the title from PythonDB database
    # flat true return the results as single values, rather than one-tuples.
    test_title = list(PythonDB.objects.values_list('title', flat=True))
    test_id = list(PythonDB.objects.values_list('id', flat=True))

    test_title_id = dict(zip(test_title, test_id))

    context = {
        'description': data.description,
        'keywords': list(data.keywords),
        'author': data.author,
        'title': data.title,
        'writer_name': data.writer_name,
        'date': data.date,
        'body': data.body,
        'related_page_link': data.related_page_link,
        'test_title_id': test_title_id,
        'current_url': current_url,
    }
    # print(request.path)
    # print(context.get('test_title_id'))
    # print(context.get('current_url'))
    return render(request, 'blog/tutorial.html', context=context)


def view_404(request, exception):
    if request.user.is_superuser:
        print(exception)
        # create and context and check the result

    return render(request, 'blog/404.html')
