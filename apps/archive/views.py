# apps/archive/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.decorators import user_is_head
from .models import Archive

@login_required
@user_is_head
def archive_list(request):
    archives = Archive.objects.all().order_by('-year')
    return render(request, 'archive/archive_list.html', {'archives': archives})

@login_required
@user_is_head
def archive_detail(request, year):
    archives = Archive.objects.filter(year=year)
    return render(request, 'archive/archive_detail.html', {'archives': archives, 'year': year})
