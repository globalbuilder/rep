# apps/training_unit/forms.py

from django import forms
from accounts.models import StudentProfile, SupervisorProfile
from training_entities.models import TrainingEntity

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['university_id', 'national_id', 'major', 'gpa', 'credit_hours_completed', 'training_status', 'cohort_year', 'supervisor', 'training_entity']
        labels = {
            'university_id': 'الرقم الجامعي',
            'national_id': 'رقم الهوية الوطنية',
            'major': 'التخصص',
            'gpa': 'المعدل التراكمي',
            'credit_hours_completed': 'عدد الساعات المكتسبة',
            'training_status': 'حالة التدريب',
            'cohort_year': 'سنة الالتحاق',
            'supervisor': 'المشرف الأكاديمي',
            'training_entity': 'جهة التدريب',
        }
        widgets = {
            'university_id': forms.TextInput(attrs={'class': 'form-control'}),
            'national_id': forms.TextInput(attrs={'class': 'form-control'}),
            'major': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
            'credit_hours_completed': forms.NumberInput(attrs={'class': 'form-control'}),
            'training_status': forms.Select(attrs={'class': 'form-control'}),
            'cohort_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'supervisor': forms.Select(attrs={'class': 'form-control'}),
            'training_entity': forms.Select(attrs={'class': 'form-control'}),
        }

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = SupervisorProfile
        fields = ['department', 'status']
        labels = {
            'department': 'القسم',
            'status': 'الحالة',
        }
        widgets = {
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class TrainingEntityForm(forms.ModelForm):
    class Meta:
        model = TrainingEntity
        fields = ['name', 'address', 'contact_person', 'contact_email', 'contact_phone', 'available_slots', 'specializations', 'gender']
        labels = {
            'name': 'اسم جهة التدريب',
            'address': 'العنوان',
            'contact_person': 'جهة الاتصال',
            'contact_email': 'البريد الإلكتروني',
            'contact_phone': 'رقم الهاتف',
            'available_slots': 'عدد الفرص المتاحة',
            'specializations': 'التخصصات',
            'gender': 'الجنس المقبول',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'available_slots': forms.NumberInput(attrs={'class': 'form-control'}),
            'specializations': forms.CheckboxSelectMultiple(),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }
