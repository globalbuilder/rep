from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'طالب'),
        ('supervisor', 'مشرف'),
        ('head', 'رئيس وحدة التدريب'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    gender = models.CharField(max_length=10, choices=(('male', 'ذكر'), ('female', 'أنثى')))

    def __str__(self):
        return self.username

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    university_id = models.CharField(max_length=20, unique=True)
    national_id = models.CharField(max_length=20, unique=True)
    major = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    credit_hours_completed = models.PositiveIntegerField()
    training_status = models.CharField(max_length=20, choices=(
        ('not_started', 'لم يبدأ'),
        ('in_progress', 'قيد التدريب'),
        ('completed', 'مكتمل')
    ))
    cohort_year = models.PositiveIntegerField()
    supervisor = models.ForeignKey('SupervisorProfile', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    training_entity = models.ForeignKey('training_entities.TrainingEntity', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class SupervisorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='supervisor_profile')
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=(
        ('active', 'نشط'),
        ('inactive', 'غير نشط')
    ))

    def __str__(self):
        return self.user.get_full_name()

class HeadProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='head_profile')
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name()

