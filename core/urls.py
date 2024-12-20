from django.urls import path
from . import views

urlpatterns = [
    path('transcribe_audio/', views.transcribe_audio, name='transcribe_audio'),
]
