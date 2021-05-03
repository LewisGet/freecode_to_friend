from django.urls import path
from .views import *

urlpatterns = [
    path('upload', image_view, name='image_upload'),
    path('fft', image_fft, name='fft'),
]
