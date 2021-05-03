from django.urls import path
from .views import *

urlpatterns = [
    path('upload', image_view, name='image_upload'),
    path('list', image_list, name='image_list'),
    path('fft/<int:id>/<int:x>-<int:y>-<int:xx>-<int:yy>', image_fft, name='fft'),
]
