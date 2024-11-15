# apps/supervisors/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import user_is_supervisor
from accounts.models import StudentProfile
from reports.models import Report
from reports.forms import ReportReviewForm
from evaluations.forms import StudentEvaluationForm
from communications.models import Message
from django.contrib import messages

@login_required
@user_is_supervisor
def dashboard(request):
    return render(request, 'supervisors/dashboard.html')

@login_required
@user_is_supervisor
def student_list(request):
    supervisor_profile = request.user.supervisor_profile
    students = supervisor_profile.students.all()
    return render(request, 'supervisors/student_list.html', {'students': students})

@login_required
@user_is_supervisor
def student_detail(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)
    return render(request, 'supervisors/student_detail.html', {'student': student})

@login_required
@user_is_supervisor
def reports(request):
    supervisor_profile = request.user.supervisor_profile
    reports = Report.objects.filter(student__student_profile__supervisor=supervisor_profile)
    return render(request, 'supervisors/reports.html', {'reports': reports})

@login_required
@user_is_supervisor
def review_report(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    if request.method == 'POST':
        form = ReportReviewForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث حالة التقرير.')
            return redirect('supervisors:reports')
    else:
        form = ReportReviewForm(instance=report)
    return render(request, 'supervisors/review_report.html', {'form': form, 'report': report})

@login_required
@user_is_supervisor
def evaluations(request):
    evaluations = request.user.given_evaluations.all()
    return render(request, 'supervisors/evaluations.html', {'evaluations': evaluations})

@login_required
@user_is_supervisor
def evaluate_student(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)
    if request.method == 'POST':
        form = StudentEvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.evaluator = request.user
            evaluation.student = student.user
            evaluation.save()
            form.save_m2m()
            messages.success(request, 'تم إرسال تقييم الطالب بنجاح.')
            return redirect('supervisors:evaluations')
    else:
        form = StudentEvaluationForm()
    return render(request, 'supervisors/evaluate_student.html', {'form': form, 'student': student})

@login_required
@user_is_supervisor
def messages(request):
    inbox = Message.objects.filter(receiver=request.user)
    sent = Message.objects.filter(sender=request.user)
    return render(request, 'supervisors/messages.html', {'inbox': inbox, 'sent': sent})
