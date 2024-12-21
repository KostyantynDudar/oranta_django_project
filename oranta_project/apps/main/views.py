from django.shortcuts import render, get_object_or_404
from apps.main.models import Article

def home_view(request):
    return render(request, "main/home.html")

def contact_view(request):
    return render(request, "main/contacts.html")

def article_list_view(request):
    articles = Article.objects.all().order_by("-created_at")
    return render(request, "main/articles.html", {"articles": articles})

def article_detail_view(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "main/article_detail.html", {"article": article})
