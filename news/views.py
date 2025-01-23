from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import News
from comments.models import Comment

def news_list(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news_list': news_list})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})

@login_required
def create_news(request):
    if not (request.user.is_super_admin() or request.user.is_admin()):
        return redirect('home')
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        News.objects.create(title=title, content=content, author=request.user)
        return redirect('news_list')
    return render(request, 'news/create_news.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import News
from .forms import NewsForm

def news_list(request):
    news_list = News.objects.all().order_by('-created_at')
    return render(request, 'news/news_list.html', {'news_list': news_list})


@login_required
def create_news(request):
    if not (request.user.is_admin or request.user.is_super_admin):
        return redirect('news_list')
        
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/create_news.html', {'form': form})