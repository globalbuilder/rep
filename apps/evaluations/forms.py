# apps/evaluations/forms.py

from django import forms
from .models import StudentEvaluation, StudentEvaluationScore, StudentEvaluationCriterion, TrainingEntityEvaluation, TrainingEntityEvaluationScore, TrainingEntityEvaluationCriterion

class StudentEvaluationForm(forms.Form):
    comments = forms.CharField(
        label='تعليقات إضافية',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        required=False
    )
    
    def __init__(self, *args, **kwargs):
        super(StudentEvaluationForm, self).__init__(*args, **kwargs)
        criteria = StudentEvaluationCriterion.objects.all()
        SCORE_CHOICES = StudentEvaluation.SCORE_CHOICES
        for criterion in criteria:
            field_name = f'criterion_{criterion.id}'
            self.fields[field_name] = forms.ChoiceField(
                label=criterion.description,
                choices=SCORE_CHOICES,
                widget=forms.RadioSelect,
                required=True
            )

class TrainingEntityEvaluationForm(forms.Form):
    comments = forms.CharField(
        label='تعليقات إضافية',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(TrainingEntityEvaluationForm, self).__init__(*args, **kwargs)
        criteria = TrainingEntityEvaluationCriterion.objects.all()
        SCORE_CHOICES = TrainingEntityEvaluation.SCORE_CHOICES
        for criterion in criteria:
            field_name = f'criterion_{criterion.id}'
            self.fields[field_name] = forms.ChoiceField(
                label=criterion.description,
                choices=SCORE_CHOICES,
                widget=forms.RadioSelect,
                required=True
            )
