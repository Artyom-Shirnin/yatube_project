from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Group, Post

POSTS = 10


def index(request):
    post_list = Post.objects.all()
    # Если порядок сортировки определен в классе Meta модели,
    # запрос будет выглядить так:
    # post_list = Post.objects.all()
    # Показывать по 10 записей на странице.
    paginator = Paginator(post_list, 10) 

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    # Отдаем в словаре контекста
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context) 

#def index(request):
 #   posts = Post.objects.all()[:POSTS]
  #  context = {
   #     'posts': posts,
    #}
    #return render(request, 'posts/index.html', context)


#def group_posts(request, slug):
    #group = get_object_or_404(Group, slug=slug)
    #posts = group.posts.all()[:POSTS]
    #context = {
        #'group': group,
        #'posts': posts,
    #}
    #return render(request, 'posts/group_list.html', context)

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    paginator = Paginator(post_list, 10)

    # Из URL извлекаем номер запрошенной страницы - это значение параметра page
    page_number = request.GET.get('page')

    # Получаем набор записей для страницы с запрошенным номером
    page_obj = paginator.get_page(page_number)
    # Отдаем в словаре контекста
    context = {
        'group': group,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)
