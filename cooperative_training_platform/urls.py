# cooperative_training_platform/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static
from cooperative_training_platform import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), 
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('students/', include(('students.urls', 'students'), namespace='students')),
    path('supervisors/', include(('supervisors.urls', 'supervisors'), namespace='supervisors')),
    path('training-unit/', include(('training_unit.urls', 'training_unit'), namespace='training_unit')),
    path('training-entities/', include(('training_entities.urls', 'training_entities'), namespace='training_entities')),
    path('evaluations/', include(('evaluations.urls', 'evaluations'), namespace='evaluations')),
    path('communications/', include(('communications.urls', 'communications'), namespace='communications')),
    path('reports/', include(('reports.urls', 'reports'), namespace='reports')),
    path('archive/', include(('archive.urls', 'archive'), namespace='archive')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'cooperative_training_platform.views.custom_404'
