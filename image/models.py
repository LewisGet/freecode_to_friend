from django.db import models


class Entity(models.Model):
    image = models.ImageField(upload_to='upload_images')
    created_at = models.DateTimeField(auto_now_add=True)
