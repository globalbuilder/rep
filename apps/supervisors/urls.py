# apps/supervisors/urls.py

from django.urls import path
from . import views

app_name = 'supervisors'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('reports/', views.reports, name='reports'),
    path('reports/<int:report_id>/', views.review_report, name='review_report'),
    path('evaluations/', views.evaluations, name='evaluations'),
    path('evaluations/student/<int:student_id>/', views.evaluate_student, name='evaluate_student'),
    path('messages/', views.messages, name='messages'),
]
