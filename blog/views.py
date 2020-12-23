from django.shortcuts import render


def index(request):
    return render(request, 'blog/index.html', context={'index': "Index Page"})

def tutorial(request):
    return render(request, 'blog/tutorial.html', context={'tutorial' : 'Tutorial Page'})