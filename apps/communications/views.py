# apps/communications/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm
from django.contrib import messages

@login_required
def inbox(request):
    messages_inbox = Message.objects.filter(receiver=request.user).order_by('-sent_at')
    return render(request, 'communications/inbox.html', {'messages': messages_inbox})

@login_required
def sent_messages(request):
    messages_sent = Message.objects.filter(sender=request.user).order_by('-sent_at')
    return render(request, 'communications/sent_messages.html', {'messages': messages_sent})

@login_required
def compose_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, sender=request.user)
        if form.is_valid():
            message_obj = form.save(commit=False)
            message_obj.sender = request.user
            message_obj.save()
            messages.success(request, 'تم إرسال الرسالة بنجاح.')
            return redirect('communications:sent_messages')
    else:
        form = MessageForm(sender=request.user)
    return render(request, 'communications/compose_message.html', {'form': form})

@login_required
def view_message(request, message_id):
    message_obj = get_object_or_404(Message, id=message_id)
    if message_obj.receiver == request.user:
        message_obj.is_read = True
        message_obj.save()
    return render(request, 'communications/view_message.html', {'message': message_obj})
