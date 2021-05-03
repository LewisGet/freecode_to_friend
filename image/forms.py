from django import forms
from .models import *


class EntityForm(forms.ModelForm):

    class Meta:
        model = Entity
        fields = ['image']
