from django.contrib import admin
from .models import (
    StudentEvaluationCriterion, StudentEvaluation, StudentEvaluationScore,
    TrainingEntityEvaluationCriterion, TrainingEntityEvaluation, TrainingEntityEvaluationScore,
)

admin.site.register(StudentEvaluationCriterion)
admin.site.register(StudentEvaluation)
admin.site.register(StudentEvaluationScore)
admin.site.register(TrainingEntityEvaluationCriterion)
admin.site.register(TrainingEntityEvaluation)
admin.site.register(TrainingEntityEvaluationScore)
