from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    articles = News.objects.all()
    return render(request, 'news/news_list.html', {'articles': articles})

def news_detail(request, id):
    article = get_object_or_404(News, id=id)
    return render(request, 'news/news_detail.html', {'article': article})
