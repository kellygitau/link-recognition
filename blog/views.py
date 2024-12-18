from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from django.utils.timezone import now
from .forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


# @login_required
def post_new(request):
    if request.method == 'POST':
        # Extract data from POST request
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.POST.get('author')
        image = request.FILES.get('image')

        # Validate inputs
        errors = {}
        if not title:
            errors['title'] = 'Title is required.'
        if not text:
            errors['text'] = 'Content is required.'
        if not author:
            errors['author'] = 'Author name is required.'

        # If there are errors, return them as JSON
        if errors:
            return JsonResponse({'success': False, 'errors': errors}, status=400)

        # Create the Post object
        post = Post(
            title=title,
            text=text,
            author=author,
            date=now(),
            image=image
        )
        post.save()
    return render(request, 'blog/post_new.html')
