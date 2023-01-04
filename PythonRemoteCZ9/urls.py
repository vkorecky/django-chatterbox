"""PythonRemoteCZ9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.models import User, Group
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import path

import accounts.views
import base.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', base.views.hello),
    path('', base.views.RoomsView.as_view(), name='rooms'),
    path('room/detail/<pk>/', base.views.room, name='room'),
    path('room/create/', base.views.RoomCreateView.as_view(), name='room_create'),
    path('room/update/<pk>', base.views.RoomUpdateView.as_view(), name='room_update'),
    path('room/delete/<pk>', base.views.RoomDeleteView.as_view(), name='room_delete'),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/password_change/', PasswordChangeView.as_view(template_name="registration/password_change.html"),
         name='password_change'),
    path('accounts/password_change_done/',
         PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),
    path('accounts/signup/', accounts.views.SignUpView.as_view(), name='signup'),

    path('search/', base.views.search, name='search')
]

handler403 = 'base.views.handler403'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        instance.groups.add(Group.objects.get(name='Participants'))
