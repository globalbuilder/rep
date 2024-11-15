# apps/communications/urls.py

from django.urls import path
from . import views

app_name = 'communications'

urlpatterns = [
    path('inbox/', views.inbox, name='inbox'),
    path('sent/', views.sent_messages, name='sent_messages'),
    path('compose/', views.compose_message, name='compose_message'),
    path('message/<int:message_id>/', views.view_message, name='view_message'),
]
