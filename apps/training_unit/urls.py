# apps/training_unit/urls.py

from django.urls import path
from . import views

app_name = 'training_unit'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.manage_students, name='manage_students'),
    path('students/<int:student_id>/edit/', views.edit_student, name='edit_student'),
    path('supervisors/', views.manage_supervisors, name='manage_supervisors'),
    path('supervisors/<int:supervisor_id>/edit/', views.edit_supervisor, name='edit_supervisor'),
    path('assign-supervisors/', views.assign_supervisors, name='assign_supervisors'),
    path('training-entities/', views.manage_training_entities, name='manage_training_entities'),
    path('training-entities/new/', views.add_training_entity, name='add_training_entity'),
    path('training-requests/', views.manage_training_requests, name='manage_training_requests'),
    path('letter-requests/', views.manage_letter_requests, name='manage_letter_requests'),
    path('deliver-letters/', views.deliver_letters, name='deliver_letters'),
    path('archive/', views.archive, name='archive'),
    path('messages/', views.messages, name='messages'),
]
