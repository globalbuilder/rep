# apps/reports/urls.py

from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('upload/', views.upload_report, name='upload_report'),
    path('student/<int:student_id>/', views.view_student_reports, name='view_student_reports'),
]
