# cooperative_training_platform/views.py

from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        # Redirect authenticated users to their dashboard based on user type
        if request.user.user_type == 'student':
            return redirect('students:dashboard')
        elif request.user.user_type == 'supervisor':
            return redirect('supervisors:dashboard')
        elif request.user.user_type == 'head':
            return redirect('training_unit:dashboard')
        else:
            return redirect('accounts:login')
    else:
        # Unauthenticated users see the welcome page
        return render(request, 'welcome.html')

def custom_404(request, exception):
    return render(request, '404.html', status=404)
