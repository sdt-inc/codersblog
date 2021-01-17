from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import resolve
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.decorators.cache import cache_page


from .models import PythonDB
from .models import BlogDB
from .models import UserEmail
from .models import SponsorDB

from codersblog.utils import add_prefix


def index(request):
    # current_url = resolve(request.path_info).url_name
    # test_data = PythonDB.objects.values_list('title')
    # print(test_data)

    data = PythonDB.objects.all()[0]
    context = {
        'description': str(data.description),
        'keywords': list(data.keywords),
        'author': str(data.author),
        'title': data.title,
        'writer_name': str(data.writer_name),
        'date': data.date,
        'body': data.body,
        'related_page_link': data.related_page_link,
        # 'test_data': test_data,
    }
    return render(request, 'blog/index.html', context=context)


def tutorial(request, slug=None):
    # data = PythonDB.objects.get(pk=pk)
    data = get_object_or_404(PythonDB, slug=slug)

    # get current url path name
    current_url = resolve(request.path_info).url_name

    # return all the title from PythonDB database
    # flat true return the results as single values, rather than one-tuples.
    titles = list(PythonDB.objects.values_list(
        'title', flat=True).order_by('-date'))
    slug_text = list(PythonDB.objects.values_list(
        'slug', flat=True).order_by('-date'))

    titles = add_prefix(titles, 'Python')
    title_slug_text = dict(zip(titles, slug_text))

    context = {
        'description': data.description,
        'keywords': list(data.keywords),
        'author': data.author,
        'title': data.title,
        'writer_name': data.writer_name,
        'date': data.date,
        'body': data.body,
        'related_page_link': data.related_page_link,
        'title_slug_text': title_slug_text,
        'current_url': current_url,
    }
    return render(request, 'blog/tutorial.html', context=context)


class BlogListView(ListView):
    model = BlogDB
    paginate_by = 5
    ordering = ['-date']

    template_name = 'blog/blog-list.html'

    def get_context_data(self, **kwargs):
        print("call list view ----------")
        context = super().get_context_data(**kwargs)
        context['current_url'] = 'blog_list'
        return context


class BlogDetailView(DetailView):

    model = BlogDB
    template_name = 'blog/blog-detail.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['object'].keywords return the list of keywords
        if len(context['object'].keywords) >= 2:
            context['related_blog'] = BlogDB.objects.filter(
                keywords__icontains=context['object'].keywords[0]).filter(keywords__icontains=context['object'].keywords[1]).order_by('-date')
        else:
            context['related_blog'] = BlogDB.objects.filter(
                keywords__icontains=context['object'].keywords[0]).order_by('-date')
        return context


def view_404(request, exception):
    print('call 404 ----------------')
    return render(request, 'blog/404.html')


def search(request):
    print('call -search ---------------')
    query = request.GET['query']
    print(request.get_full_path())
    data = BlogDB.objects.filter(title__icontains=query).order_by('-date')

    return render(request, 'blog/search.html', {'data': data})


def Editor(request):
    return render(request, 'blog/editor.html')


def UserAdded(request):
    if request.method == 'POST':
        UserEmail(email=request.POST['useremail']).save()
    return redirect('/')


def sponsors(request):
    data = SponsorDB.objects.all()

    context = {
        'sponsors_data': data,
    }
    return render(request, 'blog/sponsors.html', context=context)


def project(request):
    context = {}
    return render(request, 'blog/project.html', context=context)
