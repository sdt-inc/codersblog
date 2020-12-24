from django.shortcuts import render
from .models import PythonDB
from django.views.generic import ListView


class BlogListView(ListView):
    model = PythonDB
    template_name = 'blog/base.html'


def index(request):
    test_data = list(PythonDB.objects.all())
    
    title_id = {}
    for td in test_data:
        print(td.title, td.id)
    
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
        'test_data': test_data,
    }
    # print(context['test_data'].title)
    # print(context.get('body'))
    return render(request, 'blog/index.html', context=context)


def tutorial(request, pk=None):
    print(pk)
    test_data = PythonDB.objects.all()
    data = PythonDB.objects.all()[2]
    context = {
        'description': data.description,
        'keywords': list(data.keywords),
        'author': data.author,
        'title': data.title,
        'writer_name': data.writer_name,
        'date': data.date,
        'body': data.body,
        'related_page_link': data.related_page_link,
        'test_data': test_data,
    }
    print(context['test_data'])
    # print(context.get('date'))
    return render(request, 'blog/tutorial.html', context=context)
