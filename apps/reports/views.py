# apps/reports/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import user_is_student, user_is_supervisor
from .forms import ReportUploadForm, ReportReviewForm
from .models import Report
from accounts.models import StudentProfile
from django.contrib import messages

@login_required
@user_is_student
def upload_report(request):
    if request.method == 'POST':
        form = ReportUploadForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.student = request.user
            report.save()
            messages.success(request, 'تم رفع التقرير بنجاح.')
            return redirect('students:reports')
    else:
        form = ReportUploadForm()
    return render(request, 'reports/upload_report.html', {'form': form})

@login_required
@user_is_supervisor
def view_student_reports(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)
    reports = Report.objects.filter(student=student.user)
    return render(request, 'reports/view_student_reports.html', {'reports': reports, 'student': student})
