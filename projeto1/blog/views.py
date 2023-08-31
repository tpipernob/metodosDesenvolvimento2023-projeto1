from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    
    return render(request, 'blog/home.html', {'posts' : posts})
