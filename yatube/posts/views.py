from django.shortcuts import render
from django.http import HttpResponse

# Главная страница
def index(request): 
    template = 'posts/index.html'
    return render(request, template)


#  Посты, отфильтрованные по группам
def group_posts(request):
    return HttpResponse('Страница групп')
