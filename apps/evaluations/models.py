# apps/evaluations/models.py

from django.db import models
from django.conf import settings

class StudentEvaluationCriterion(models.Model):
    CRITERIA_CHOICES = (
        (1, 'المحافظة على أوقات الدوام.'),
        (2, 'الالتزام بإجراءات وأنظمة العمل.'),
        (3, 'المظهر العام للمتدرب.'),
        # Add all other criteria up to 10
    )

    criterion_number = models.PositiveIntegerField('رقم المعيار', choices=CRITERIA_CHOICES)
    description = models.CharField('وصف المعيار', max_length=255)

    def __str__(self):
        return f'{self.get_criterion_number_display()}'


class StudentEvaluation(models.Model):
    SCORE_CHOICES = (
        (10, 'ممتاز'),
        (8, 'جيد جدا'),
        (6, 'جيد'),
        (4, 'مقبول'),
        (2, 'ضعيف'),
    )

    evaluator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_evaluations_given')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_evaluations_received')
    date_submitted = models.DateTimeField('تاريخ التقديم', auto_now_add=True)
    total_score = models.PositiveIntegerField('المجموع النهائي', default=0)

    def __str__(self):
        return f'تقييم الطالب {self.student.get_full_name()}'

    def calculate_total_score(self):
        total = sum(item.score for item in self.criteria_scores.all())
        self.total_score = total
        self.save()
        return total

class StudentEvaluationScore(models.Model):
    evaluation = models.ForeignKey(StudentEvaluation, on_delete=models.CASCADE, related_name='criteria_scores')
    criterion = models.ForeignKey(StudentEvaluationCriterion, on_delete=models.CASCADE)
    score = models.PositiveIntegerField('الدرجة', choices=StudentEvaluation.SCORE_CHOICES)

    def __str__(self):
        return f'{self.criterion.description} - {self.score}'

class TrainingEntityEvaluationCriterion(models.Model):
    CRITERIA_CHOICES = (
        (1, 'جدية التدريب.'),
        (2, 'الخبرة التي يقدمها التدريب.'),
        (3, 'مناسبة مكان التدريب.'),
        # Add all other criteria up to 10
    )

    criterion_number = models.PositiveIntegerField('رقم المعيار', choices=CRITERIA_CHOICES)
    description = models.CharField('وصف المعيار', max_length=255)

    def __str__(self):
        return f'{self.get_criterion_number_display()}'

class TrainingEntityEvaluation(models.Model):
    SCORE_CHOICES = (
        (10, 'ممتاز'),
        (8, 'جيد جدا'),
        (6, 'جيد'),
        (4, 'مقبول'),
        (2, 'ضعيف'),
    )

    evaluator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='entity_evaluations_given')
    training_entity = models.ForeignKey('training_entities.TrainingEntity', on_delete=models.CASCADE, related_name='evaluations_received')
    date_submitted = models.DateTimeField('تاريخ التقديم', auto_now_add=True)
    total_score = models.PositiveIntegerField('المجموع النهائي', default=0)

    def __str__(self):
        return f'تقييم جهة التدريب {self.training_entity.name}'

    def calculate_total_score(self):
        total = sum(item.score for item in self.criteria_scores.all())
        self.total_score = total
        self.save()
        return total
class TrainingEntityEvaluationScore(models.Model):
    evaluation = models.ForeignKey(TrainingEntityEvaluation, on_delete=models.CASCADE, related_name='criteria_scores')
    criterion = models.ForeignKey(TrainingEntityEvaluationCriterion, on_delete=models.CASCADE)
    score = models.PositiveIntegerField('الدرجة', choices=TrainingEntityEvaluation.SCORE_CHOICES)

    def __str__(self):
        return f'{self.criterion.description} - {self.score}'
