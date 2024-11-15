# apps/archive/urls.py

from django.urls import path
from . import views

app_name = 'archive'

urlpatterns = [
    path('', views.archive_list, name='archive_list'),
    path('<int:year>/', views.archive_detail, name='archive_detail'),
]
