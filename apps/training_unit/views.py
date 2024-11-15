# apps/training_unit/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import user_is_head
from accounts.models import StudentProfile, SupervisorProfile
from training_entities.models import TrainingEntity
from students.models import TrainingRequest, LetterRequest
from .forms import StudentForm, SupervisorForm, TrainingEntityForm
from communications.models import Message
from django.contrib import messages

@login_required
@user_is_head
def dashboard(request):
    return render(request, 'training_unit/dashboard.html')

@login_required
@user_is_head
def manage_students(request):
    students = StudentProfile.objects.all()
    return render(request, 'training_unit/manage_students.html', {'students': students})

@login_required
@user_is_head
def edit_student(request, student_id):
    student = get_object_or_404(StudentProfile, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث بيانات الطالب.')
            return redirect('training_unit:manage_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'training_unit/edit_student.html', {'form': form})

@login_required
@user_is_head
def manage_supervisors(request):
    supervisors = SupervisorProfile.objects.all()
    return render(request, 'training_unit/manage_supervisors.html', {'supervisors': supervisors})

@login_required
@user_is_head
def edit_supervisor(request, supervisor_id):
    supervisor = get_object_or_404(SupervisorProfile, id=supervisor_id)
    if request.method == 'POST':
        form = SupervisorForm(request.POST, instance=supervisor)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث بيانات المشرف.')
            return redirect('training_unit:manage_supervisors')
    else:
        form = SupervisorForm(instance=supervisor)
    return render(request, 'training_unit/edit_supervisor.html', {'form': form})

@login_required
@user_is_head
def assign_supervisors(request):
    # Implement logic to assign supervisors to students
    return render(request, 'training_unit/assign_supervisors.html')

@login_required
@user_is_head
def manage_training_entities(request):
    entities = TrainingEntity.objects.all()
    return render(request, 'training_unit/manage_training_entities.html', {'entities': entities})

@login_required
@user_is_head
def add_training_entity(request):
    if request.method == 'POST':
        form = TrainingEntityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة جهة تدريب جديدة.')
            return redirect('training_unit:manage_training_entities')
    else:
        form = TrainingEntityForm()
    return render(request, 'training_unit/add_training_entity.html', {'form': form})

@login_required
@user_is_head
def manage_training_requests(request):
    requests = TrainingRequest.objects.all()
    return render(request, 'training_unit/manage_training_requests.html', {'requests': requests})

@login_required
@user_is_head
def manage_letter_requests(request):
    requests = LetterRequest.objects.all()
    return render(request, 'training_unit/manage_letter_requests.html', {'requests': requests})

@login_required
@user_is_head
def deliver_letters(request):
    # Implement logic to deliver letters to students
    return render(request, 'training_unit/deliver_letters.html')

@login_required
@user_is_head
def archive(request):
    # Implement logic for archiving data
    return render(request, 'training_unit/archive.html')

@login_required
@user_is_head
def messages(request):
    inbox = Message.objects.filter(receiver=request.user)
    sent = Message.objects.filter(sender=request.user)
    return render(request, 'training_unit/messages.html', {'inbox': inbox, 'sent': sent})
