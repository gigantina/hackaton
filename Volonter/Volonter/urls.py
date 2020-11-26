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
from django.contrib.auth import as auth_views
from . import views

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
	
	#url(r'^change-password/$', views.change_password, name='change_password'),
	url(r'^reset_password/$', auth_views.PasswordResetView.as_view(template_name="password_reset.html"), name='reset_password'),
	url(r'^reset_password_sent/$', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name='password_reset_done'),
	url(r'^reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name='password_reset_confirm'),
	url(r'^reset_password_complete/$', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name='password_reset_complete'),
]










