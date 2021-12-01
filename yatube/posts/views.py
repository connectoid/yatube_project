from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_posts(request, slug):
    return HttpResponse('Посты, отфильтрованные по группам')
