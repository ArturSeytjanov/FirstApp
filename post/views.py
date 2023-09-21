from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from .models import Post

def homePage(request):
    return render(request, 'post/home.html')

def aboutPage(request):
    #SQL -> SELECT * FROM Post;
    #SQL -> SELECT * FROM Post WHERE id = 1;
    posts = Post.objects.all()
    #text = Post.objects.get(id=1)
    context = {
        'posts': posts
    }
    return render(request, 'post/about.html', context)

def aboutDetail(request, pk):
    #post = get_object_or_404(Post, pk=pk)
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return render(request, 'post/404.html' )
    
    context = {
        'post': post
    }
    return render(request, 'post/about_detail.html',context)

def servicesPage(request):
    return render(request, 'post/services.html')

def contactPage(request):
    return render(request, 'post/contact.html')
