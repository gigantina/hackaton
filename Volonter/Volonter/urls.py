"""Volonter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TestApp import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('', views.main_page),
    path('donate/', views.donate_page),
    path('events', views.events_page),
    path('admin/', admin.site.urls)
	path('login/', auth_views.LoginView.as_view()),
    path('register/', views.RegisterFormView.as_view()),
    path('logout/', views.logout_view),
	path('', include("django.contrib.auth.urls")),
	url(r'^logout', views.logout, name='logout'),
	url(r'^profile/$', views.view_profile, name='view_profile'),
	url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
	path('/comment/', AddCommentView.as_view(), name='add_comment'),
	url(r'^change-password/$', views.change_password, name='change_password'),
	url(r'^reset_password/$', password_reset, name='reset_password'),
	url(r'^reset_password/done/$', password_reset_done, name='reset_password_done'),
	url(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?)$P<token>+/$', password_reset_confirm, name='reset_password_confirm'),
	url(r'^reset_password/complete/$', password_reset_complete, name='reset_password_complete'),
]
