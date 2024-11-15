# Generated by Django 5.1.2 on 2024-11-08 08:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('training_entities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LetterRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter_type', models.CharField(choices=[('official', 'رسمي'), ('recommendation', 'توصية')], max_length=20, verbose_name='نوع الخطاب')),
                ('date_submitted', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ التقديم')),
                ('status', models.CharField(choices=[('pending', 'قيد الانتظار'), ('approved', 'مقبول'), ('rejected', 'مرفوض')], default='pending', max_length=20, verbose_name='الحالة')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='تعليقات')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='letter_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrainingRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_submitted', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ التقديم')),
                ('status', models.CharField(choices=[('pending', 'قيد الانتظار'), ('approved', 'مقبول'), ('rejected', 'مرفوض')], default='pending', max_length=20, verbose_name='الحالة')),
                ('comments', models.TextField(blank=True, null=True, verbose_name='تعليقات')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_requests', to=settings.AUTH_USER_MODEL)),
                ('training_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='training_entities.trainingentity', verbose_name='جهة التدريب')),
            ],
        ),
    ]
