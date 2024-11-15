from django.db import models
from django.conf import settings
from training_entities.models import TrainingEntity

class TrainingRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'قيد الانتظار'),
        ('approved', 'مقبول'),
        ('rejected', 'مرفوض'),
    )

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='training_requests')
    training_entity = models.ForeignKey(TrainingEntity, on_delete=models.CASCADE, verbose_name='جهة التدريب')
    date_submitted = models.DateTimeField('تاريخ التقديم', auto_now_add=True)
    status = models.CharField('الحالة', max_length=20, choices=STATUS_CHOICES, default='pending')
    comments = models.TextField('تعليقات', blank=True, null=True)

    def __str__(self):
        return f'{self.student.get_full_name()} - {self.training_entity.name}'

class LetterRequest(models.Model):
    LETTER_TYPE_CHOICES = (
        ('official', 'رسمي'),
        ('recommendation', 'توصية'),
    )

    STATUS_CHOICES = (
        ('pending', 'قيد الانتظار'),
        ('approved', 'مقبول'),
        ('rejected', 'مرفوض'),
    )

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='letter_requests')
    letter_type = models.CharField('نوع الخطاب', max_length=20, choices=LETTER_TYPE_CHOICES)
    date_submitted = models.DateTimeField('تاريخ التقديم', auto_now_add=True)
    status = models.CharField('الحالة', max_length=20, choices=STATUS_CHOICES, default='pending')
    comments = models.TextField('تعليقات', blank=True, null=True)

    def __str__(self):
        return f'{self.student.get_full_name()} - {self.get_letter_type_display()}'

