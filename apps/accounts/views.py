# apps/accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomAuthenticationForm, PasswordChangeForm, ProfileForm

def login_view(request):
    if request.user.is_authenticated:
        # Redirect authenticated users to their dashboard
        if request.user.user_type == 'student':
            return redirect('students:dashboard')
        elif request.user.user_type == 'supervisor':
            return redirect('supervisors:dashboard')
        elif request.user.user_type == 'head':
            return redirect('training_unit:dashboard')
        else:
            return redirect('accounts:login')
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to appropriate dashboard based on user type
                if user.user_type == 'student':
                    return redirect('students:dashboard')
                elif user.user_type == 'supervisor':
                    return redirect('supervisors:dashboard')
                elif user.user_type == 'head':
                    return redirect('training_unit:dashboard')
                else:
                    return redirect('accounts:login')
            else:
                messages.error(request, 'خطأ في اسم المستخدم أو كلمة المرور')
        else:
            messages.error(request, 'خطأ في البيانات المدخلة')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user)
        password_form = PasswordChangeForm(user=request.user, data=request.POST)
        if profile_form.is_valid() and password_form.is_valid():
            profile_form.save()
            password_form.save()
            update_session_auth_hash(request, password_form.user)  # Important!
            messages.success(request, 'تم تحديث الملف الشخصي وكلمة المرور بنجاح.')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'يرجى تصحيح الأخطاء أدناه.')
    else:
        profile_form = ProfileForm(instance=request.user)
        password_form = PasswordChangeForm(user=request.user)
    context = {
        'profile_form': profile_form,
        'password_form': password_form,
    }
    return render(request, 'accounts/profile.html', context)