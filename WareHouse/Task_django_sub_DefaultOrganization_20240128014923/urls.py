'''
This file defines the URLs for the Task views
'''
from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.task_list, name='task_list'),
]