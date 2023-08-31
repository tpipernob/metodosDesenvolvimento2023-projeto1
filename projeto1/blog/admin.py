from django.contrib import admin

# Register your models here.
from blog.models import Post

# admin.site.register(Post)
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data')
    list_filter = ('autor', 'data')
    search_fields = ('conteudo',)
    date_hierarchy = ('data')
