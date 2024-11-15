# apps/reports/forms.py

from django import forms
from .models import Report

class ReportUploadForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['file', 'report_type']
        labels = {
            'file': 'ملف التقرير',
            'report_type': 'نوع التقرير',
        }
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'report_type': forms.Select(attrs={'class': 'form-control'}),
        }

class ReportReviewForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['supervisor_comments', 'status']
        labels = {
            'supervisor_comments': 'تعليقات المشرف',
            'status': 'الحالة',
        }
        widgets = {
            'supervisor_comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
