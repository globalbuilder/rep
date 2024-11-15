# apps/evaluations/urls.py

from django.urls import path
from . import views

app_name = 'evaluations'

urlpatterns = [
    path('student-evaluation/<int:student_id>/', views.student_evaluation, name='student_evaluation'),
    path('training-entity-evaluation/<int:entity_id>/', views.training_entity_evaluation, name='training_entity_evaluation'),
]
