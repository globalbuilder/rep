from django.db import models

class Specialization(models.Model):
    name = models.CharField('اسم التخصص', max_length=255)

    def __str__(self):
        return self.name

class TrainingEntity(models.Model):
    GENDER_CHOICES = (
        ('male', 'ذكر'),
        ('female', 'أنثى'),
        ('both', 'كلاهما'),
    )

    name = models.CharField('اسم جهة التدريب', max_length=255)
    address = models.TextField('العنوان')
    contact_person = models.CharField('اسم جهة الاتصال', max_length=255)
    contact_email = models.EmailField('البريد الإلكتروني لجهة الاتصال')
    contact_phone = models.CharField('رقم هاتف جهة الاتصال', max_length=20)
    available_slots = models.PositiveIntegerField('عدد الفرص المتاحة')
    specializations = models.ManyToManyField(Specialization, verbose_name='التخصصات')
    gender = models.CharField('الجنس المقبول', max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name
