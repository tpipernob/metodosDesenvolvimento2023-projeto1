from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list.as_view(), name="home"),
    path('post/<int:pk>', views.post_detalhe.as_view(), name="post-detalhe"),
    path('post/new/', views.post_new.as_view(), name="post-new"),
    path('post/<int:pk>/edit', views.post_edit.as_view(), name="post-edit"),
    path('post/<int:pk>/delete', views.post_delete.as_view(), name="post-delete"),

]
