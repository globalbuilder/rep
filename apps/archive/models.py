from django.db import models
from django.conf import settings

class Archive(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='archives')
    year = models.PositiveIntegerField('السنة')
    data = models.JSONField('البيانات')

    def __str__(self):
        return f'أرشيف {self.student.get_full_name()} - {self.year}'
