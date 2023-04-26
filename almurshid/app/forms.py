from django import forms
from django.forms.widgets import Textarea, TextInput

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ("is_active",)
        widgets = {
            "name": TextInput(
                attrs={"class": "required form-control", "placeholder": "Your Name"}
            ),
            "message": Textarea(
                attrs={"class": "required form-control", "placeholder": "Message"}
            ),
        }
