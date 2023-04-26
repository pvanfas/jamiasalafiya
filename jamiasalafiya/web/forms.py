from django import forms
from django.forms.widgets import Select

from .models import Result


class ResultForm(forms.Form):
    choice = forms.ModelChoiceField(
        queryset=Result.objects.filter(is_active=True), empty_label="Select the course"
    )
