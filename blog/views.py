from django.shortcuts import get_object_or_404, render
from django.urls import resolve
from django.views.generic import ListView

from .models import PythonDB


def index(request):
    # current_url = resolve(request.path_info).url_name
    # test_data = PythonDB.objects.values_list('title')
    # print(test_data)

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
    titles = list(PythonDB.objects.values_list('title', flat=True))
    primary_keys = list(PythonDB.objects.values_list('id', flat=True))

    title_primary_keys = dict(zip(titles, primary_keys))

    context = {
        'description': data.description,
        'keywords': list(data.keywords),
        'author': data.author,
        'title': data.title,
        'writer_name': data.writer_name,
        'date': data.date,
        'body': data.body,
        'related_page_link': data.related_page_link,
        'title_primary_keys': title_primary_keys,
        'current_url': current_url,
    }
    # print(request.path)
    # print(context.get('test_title_id'))
    print(context.get('current_url'))
    return render(request, 'blog/tutorial.html', context=context)


def view_404(request, exception):
    if request.user.is_superuser:
        print(exception)
        # create and context and check the result

    return render(request, 'blog/404.html')


def search(request):
    query = request.GET['query']
    data = PythonDB.objects.filter(title__icontains=query)

    return render(request, 'blog/search.html', {'data': data})
