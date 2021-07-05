from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


@login_required
def post(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)


