from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Message, Chat, CustomUser


class MessageForm(forms.Form):
    model = Message
    message = forms.CharField(widget=forms.Textarea)


class ChatCreateForm(forms.ModelForm):
    user = forms.CharField(max_length=30, label="User name")
    #chat = forms.CharField(max_length=100, label="Chat name")

    class Meta:
        model = Chat
        fields = ['Chat_name']
        labels = {
            'Chat_name': _('Chat name'),
        }