from django.urls import path

from django_102.tasks.views import home

urlpatterns = (
    path('', home),
)