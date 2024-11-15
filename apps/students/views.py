# apps/students/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.decorators import user_is_student
from reports.forms import ReportUploadForm
from .forms import TrainingRequestForm, LetterRequestForm
from .models import TrainingRequest, LetterRequest
from reports.models import Report
from communications.models import Message
from evaluations.forms import TrainingEntityEvaluationForm
from evaluations.models import TrainingEntityEvaluation
from django.contrib import messages

@login_required
@user_is_student
def dashboard(request):
    return render(request, 'students/dashboard.html')

@login_required
@user_is_student
def training_requests(request):
    requests = TrainingRequest.objects.filter(student=request.user)
    return render(request, 'students/training_requests.html', {'requests': requests})

@login_required
@user_is_student
def new_training_request(request):
    if request.method == 'POST':
        form = TrainingRequestForm(request.POST)
        if form.is_valid():
            training_request = form.save(commit=False)
            training_request.student = request.user
            training_request.save()
            messages.success(request, 'تم تقديم طلب التدريب بنجاح.')
            return redirect('students:training_requests')
    else:
        form = TrainingRequestForm()
    return render(request, 'students/new_training_request.html', {'form': form})

@login_required
@user_is_student
def letter_requests(request):
    requests = LetterRequest.objects.filter(student=request.user)
    return render(request, 'students/letter_requests.html', {'requests': requests})

@login_required
@user_is_student
def new_letter_request(request):
    if request.method == 'POST':
        form = LetterRequestForm(request.POST)
        if form.is_valid():
            letter_request = form.save(commit=False)
            letter_request.student = request.user
            letter_request.save()
            messages.success(request, 'تم تقديم طلب الخطاب بنجاح.')
            return redirect('students:letter_requests')
    else:
        form = LetterRequestForm()
    return render(request, 'students/new_letter_request.html', {'form': form})

@login_required
@user_is_student
def reports(request):
    reports = Report.objects.filter(student=request.user)
    return render(request, 'students/reports.html', {'reports': reports})

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
    return render(request, 'students/upload_report.html', {'form': form})

@login_required
@user_is_student
def evaluations(request):
    evaluations = request.user.student_evaluations_received.all()
    return render(request, 'students/evaluations.html', {'evaluations': evaluations})

@login_required
@user_is_student
def evaluate_training_entity(request):
    if request.method == 'POST':
        form = TrainingEntityEvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.evaluator = request.user
            evaluation.save()
            form.save_m2m()
            messages.success(request, 'تم إرسال تقييم جهة التدريب بنجاح.')
            return redirect('students:evaluations')
    else:
        form = TrainingEntityEvaluationForm()
    return render(request, 'students/evaluate_training_entity.html', {'form': form})

@login_required
@user_is_student
def messages(request):
    inbox = Message.objects.filter(receiver=request.user)
    sent = Message.objects.filter(sender=request.user)
    return render(request, 'students/messages.html', {'inbox': inbox, 'sent': sent})
