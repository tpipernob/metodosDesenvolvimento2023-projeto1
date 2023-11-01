from django.shortcuts import render
from .models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class post_list(generic.ListView):
    modelo = Post
    template_name = 'blog/home.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-data')[:3]

class post_detalhe(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'blog/post_detalhe.html'
