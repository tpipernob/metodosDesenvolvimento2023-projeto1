from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name="home"),
    path('post/<int:post_id>', views.post_detalhe, name="post-detalhe"),

]
