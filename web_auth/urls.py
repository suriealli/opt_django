#coding=utf-8
from django.conf.urls import url, include
# from django.contrib import admin
from web_auth import views

urlpatterns = [
    url(r'^register/$', views.register, name='register'), # 注册链接
    # url(r'^login/$', views.user_login, name='login'), # 登录链接
    # url(r'^logout/$', views.user_logout, name='logout'),#登出
    # url(r'^restricted/', views.restricted, name='restricted'),# 权限把控
    ]