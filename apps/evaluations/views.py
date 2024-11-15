# apps/evaluations/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import user_is_supervisor, user_is_student
from .forms import StudentEvaluationForm, TrainingEntityEvaluationForm
from accounts.models import StudentProfile
from training_entities.models import TrainingEntity
from django.contrib import messages

@login_required
@user_is_supervisor
def student_evaluation(request, student_id):
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
            return redirect('supervisors:student_list')
    else:
        form = StudentEvaluationForm()
    return render(request, 'evaluations/student_evaluation.html', {'form': form, 'student': student})

@login_required
@user_is_student
def training_entity_evaluation(request, entity_id):
    entity = get_object_or_404(TrainingEntity, id=entity_id)
    if request.method == 'POST':
        form = TrainingEntityEvaluationForm(request.POST)
        if form.is_valid():
            evaluation = form.save(commit=False)
            evaluation.evaluator = request.user
            evaluation.training_entity = entity
            evaluation.save()
            form.save_m2m()
            messages.success(request, 'تم إرسال تقييم جهة التدريب بنجاح.')
            return redirect('students:dashboard')
    else:
        form = TrainingEntityEvaluationForm()
    return render(request, 'evaluations/training_entity_evaluation.html', {'form': form, 'entity': entity})
