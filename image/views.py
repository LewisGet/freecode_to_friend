from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def image_view(request):
    form = EntityForm()

    if request.method == 'POST':
        form = EntityForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('fft')

    return render(request, 'base_form.html', {'form': form})

def image_fft(request, id, x, y, xx, yy):
    entity = Entity.objects.get(pk=id)

    return render(request, 'base_view.html', {'entity': entity})
