from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


def image_view(request):
    form = EntityForm()

    if request.method == 'POST':
        form = EntityForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('fft')

    return render(request, 'base_form.html', {'form': form})

def image_fft(request):
    pass
