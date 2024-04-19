
from django.contrib import admin
from django.urls import path, include

from .views import TaskViewSet, login_view, register_view
from rest_framework import routers


router = routers.DefaultRouter();


router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', login_view, name='login'),
    path('auth/register/', register_view, name='register'),
]
