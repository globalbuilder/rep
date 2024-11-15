# apps/training_entities/urls.py

from django.urls import path
from . import views

app_name = 'training_entities'

urlpatterns = [
    path('list/', views.entity_list, name='entity_list'),
    path('<int:entity_id>/', views.entity_detail, name='entity_detail'),
]
