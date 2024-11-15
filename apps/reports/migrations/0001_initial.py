# Generated by Django 5.1.2 on 2024-11-08 08:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='reports/', verbose_name='ملف التقرير')),
                ('report_type', models.CharField(choices=[('weekly', 'أسبوعي'), ('final', 'نهائي')], max_length=20, verbose_name='نوع التقرير')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الرفع')),
                ('supervisor_comments', models.TextField(blank=True, null=True, verbose_name='تعليقات المشرف')),
                ('status', models.CharField(choices=[('submitted', 'تم الإرسال'), ('under_review', 'قيد المراجعة'), ('approved', 'مقبول'), ('needs_revision', 'يحتاج إلى تعديل')], default='submitted', max_length=20, verbose_name='الحالة')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
