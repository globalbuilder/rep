# apps/students/forms.py

from django import forms
from .models import TrainingRequest, LetterRequest
from training_entities.models import TrainingEntity

class TrainingRequestForm(forms.ModelForm):
    class Meta:
        model = TrainingRequest
        fields = ['training_entity', 'comments']
        labels = {
            'training_entity': 'جهة التدريب',
            'comments': 'تعليقات',
        }
        widgets = {
            'training_entity': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class LetterRequestForm(forms.ModelForm):
    class Meta:
        model = LetterRequest
        fields = ['letter_type', 'comments']
        labels = {
            'letter_type': 'نوع الخطاب',
            'comments': 'تعليقات',
        }
        widgets = {
            'letter_type': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
