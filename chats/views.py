from django.views.generic import TemplateView
from .models import Message


class HomeChatView(TemplateView):
    template_name = 'chat.html'
    model = Message
