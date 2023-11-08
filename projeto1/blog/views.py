from django.shortcuts import render
from .models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class post_list(generic.ListView):
    modelo = Post
    template_name = 'blog/home.html'

    def get_queryset(self):
        return Post.objects.all().order_by('-data')[:3]

class post_detalhe(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'blog/post_detalhe.html'

class post_new(generic.CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = '__all__'

class post_edit(generic.UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ('titulo', 'conteudo')

class post_delete(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')