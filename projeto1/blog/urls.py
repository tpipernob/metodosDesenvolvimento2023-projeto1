from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list.as_view(), name="home"),
    path('post/<int:pk>', views.post_detalhe.as_view(), name="post-detalhe"),

]
