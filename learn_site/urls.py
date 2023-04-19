from django.urls import path, include

from learn_site.views import index, task

urlpatterns = [
    path('', index),
    path('tasks/<int:pk>/', task),
]