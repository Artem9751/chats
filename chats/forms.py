from django import forms

from .models import Message

class MessageForm(forms.Form):
    model = Message
    message = forms.CharField(widget=forms.Textarea)