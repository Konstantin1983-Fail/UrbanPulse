from django.core.paginator import Paginator
from django.shortcuts import render
from .models import News

def news(request):
    # Получаем все новости из базы данных
    news_list = News.objects.all().order_by('-date', '-id')  # Сортировка по дате и ID

    # Создаем объект Paginator с 5 новостями на страницу
    paginator = Paginator(news_list, 5)

    # Получаем номер текущей страницы из параметра GET
    page_number = request.GET.get('page')

    # Получаем объект страницы
    page_obj = paginator.get_page(page_number)

    # Передаем объект страницы в контекст шаблона
    context = {
        'news': page_obj,
    }

    return render(request, 'task1/news.html', context)