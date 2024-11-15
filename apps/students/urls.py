# apps/students/urls.py

from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('training-requests/', views.training_requests, name='training_requests'),
    path('training-requests/new/', views.new_training_request, name='new_training_request'),
    path('letter-requests/', views.letter_requests, name='letter_requests'),
    path('letter-requests/new/', views.new_letter_request, name='new_letter_request'),
    path('reports/', views.reports, name='reports'),
    path('reports/upload/', views.upload_report, name='upload_report'),
    path('evaluations/', views.evaluations, name='evaluations'),
    path('evaluations/training-entity/', views.evaluate_training_entity, name='evaluate_training_entity'),
    path('messages/', views.messages, name='messages'),
]
