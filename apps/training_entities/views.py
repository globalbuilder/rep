# apps/training_entities/views.py

from django.shortcuts import render, get_object_or_404
from .models import TrainingEntity
from django.contrib.auth.decorators import login_required

@login_required
def entity_list(request):
    entities = TrainingEntity.objects.all()
    return render(request, 'training_entities/entity_list.html', {'entities': entities})

@login_required
def entity_detail(request, entity_id):
    entity = get_object_or_404(TrainingEntity, id=entity_id)
    return render(request, 'training_entities/entity_detail.html', {'entity': entity})
