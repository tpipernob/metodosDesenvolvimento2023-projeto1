from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    
    return render(request, 'blog/home.html', {'posts' : posts})


def post_detalhe(request, post_id):
    post = Post.objects.get(pk=post_id)

    return render(request, 'blog/post_detalhe.html', {'post' : post})
