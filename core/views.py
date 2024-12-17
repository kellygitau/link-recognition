from datetime import timezone
from django.shortcuts import redirect, render

from blog.forms import PostForm
from blog.models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')