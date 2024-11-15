from django.db import models
from django.conf import settings

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField('الموضوع', max_length=255)
    content = models.TextField('المحتوى')
    date_sent = models.DateTimeField('تاريخ الإرسال', auto_now_add=True)
    is_read = models.BooleanField('مقروء', default=False)

    def __str__(self):
        return f'رسالة من {self.sender.get_full_name()} إلى {self.receiver.get_full_name()}'
