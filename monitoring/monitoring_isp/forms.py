
from django import forms

from .models import *


class UpdateMonitoringForm(forms.Form):
    nomeruch = forms.ModelChoiceField(queryset=Uch.objects.all())
