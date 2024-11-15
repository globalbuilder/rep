# apps/communications/forms.py

from django import forms
from .models import Message
from django.contrib.auth import get_user_model

User = get_user_model()

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'content']
        labels = {
            'receiver': 'المستلم',
            'subject': 'الموضوع',
            'content': 'المحتوى',
        }
        widgets = {
            'receiver': forms.Select(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
    
    def __init__(self, *args, **kwargs):
        sender = kwargs.pop('sender', None)
        super(MessageForm, self).__init__(*args, **kwargs)
        if sender:
            self.fields['receiver'].queryset = User.objects.exclude(id=sender.id)
