from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files import File
from django.conf import settings
from .models import *
from .forms import *
import os


def image_view(request):
    form = EntityForm()

    if request.method == 'POST':
        form = EntityForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('image_list')

    return render(request, 'base_form.html', {'form': form})


def image_fft(request, id, x, y, xx, yy):
    """
    this code just paste on

    :param request:
    :param id: image entity id
    :param x: start cut x
    :param y: start cut y
    :param xx: end cut x
    :param yy: end cut y
    :return:
    """
    import hashlib
    import cv2
    import numpy as np


    entity = Entity.objects.get(pk=id)
    _, ext = os.path.splitext(entity.image.path)

    img = cv2.imread(entity.image.path, 0)
    img = img[y:yy, x:xx]

    #this code just paste on
    f = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    f_shift = np.fft.fftshift(f)
    f_complex = f_shift[:, :, 0] + 1j * f_shift[:, :, 1]
    f_abs = np.abs(f_complex) + 1
    f_bounded = 20 * np.log(f_abs)
    f_img = 255 * f_bounded / np.max(f_bounded)
    f_img = f_img.astype(np.uint8)
    # end paste on

    md5_name = hashlib.md5(str(f_img).encode()).hexdigest()
    cache_file_path = os.path.join(settings.FFT_CACHE, md5_name + ext)
    cv2.imwrite(cache_file_path, f_img)

    if not os.path.exists(settings.FFT_CACHE):
        os.makedirs(settings.FFT_CACHE)

    cf = open(cache_file_path, 'rb')

    entity.fft_image = File(cf, name=md5_name)
    entity.save()

    return redirect('image_list')


def image_list(request):
    entities = Entity.objects.all()

    return render(request, 'base_list.html', {'entities': entities})

