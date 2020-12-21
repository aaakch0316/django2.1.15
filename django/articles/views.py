from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    content = {
        'articles' : articles
    }
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)