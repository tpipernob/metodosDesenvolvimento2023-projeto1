from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.titulo
    
    class Meta:
        ordering = ['-data']
