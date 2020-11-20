#!/usr/bin/env python
# -- coding = 'utf-8' --
# Author WangBin
# Python Version 3.6.6
# @Software:PyCharm
# @File : urls.py
# @Date  : 2020/11/20
# @Email  : 560331

from django.urls import path

# 正在部署的应用的名称
from article import views

app_name = 'article'

urlpatterns = [
    # 目前还没有urls
    path('article-list/', views.article_list, name='article_list'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
]