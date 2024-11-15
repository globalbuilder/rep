from django.db import models
from django.conf import settings

class Report(models.Model):
    REPORT_TYPE_CHOICES = (
        ('weekly', 'أسبوعي'),
        ('final', 'نهائي'),
    )

    STATUS_CHOICES = (
        ('submitted', 'تم الإرسال'),
        ('under_review', 'قيد المراجعة'),
        ('approved', 'مقبول'),
        ('needs_revision', 'يحتاج إلى تعديل'),
    )

    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reports')
    file = models.FileField('ملف التقرير', upload_to='reports/')
    report_type = models.CharField('نوع التقرير', max_length=20, choices=REPORT_TYPE_CHOICES)
    date_uploaded = models.DateTimeField('تاريخ الرفع', auto_now_add=True)
    supervisor_comments = models.TextField('تعليقات المشرف', blank=True, null=True)
    status = models.CharField('الحالة', max_length=20, choices=STATUS_CHOICES, default='submitted')

    def __str__(self):
        return f'{self.student.get_full_name()} - {self.get_report_type_display()}'
