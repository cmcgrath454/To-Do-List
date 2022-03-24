"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from todolistapp import views

urlpatterns = [
    path('', views.view_all_tasks, name=""),
    path('new_task', views.new_task, name="new_task"),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('delete/<int:id>/', views.delete, name='delete_task'),
    path('markdone/<int:id>/', views.mark_done, name='mark_done'),
    path('completed', views.view_completed_tasks, name='completed'),
    path('admin/', admin.site.urls),
]
