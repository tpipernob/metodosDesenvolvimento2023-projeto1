from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField


class Post(models.Model):
    titulo = models.CharField(max_length=300)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = RichTextField()
    data = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.titulo
    
    def get_absolute_url(self):
        return u'/post/%d' % self.id

    
    class Meta:
        ordering = ['-data']
