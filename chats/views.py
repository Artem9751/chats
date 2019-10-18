from django.views.generic import ListView
from .models import Message
from .forms import MessageForm
from django.utils import timezone
from django.shortcuts import render


class HomeChatView(ListView):
    template_name = 'chat.html'
    model = Message
    form_class = MessageForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            message = Message()
            message.message_text = request.POST.get("message")
            message.message_time = timezone.now()
            message.message_author = request.user
            message.save()
        return self.render_page(request)

    def get(self, request):
        """ Accepts Get request and render template with a call to the render_page  """
        return self.render_page(request)

    def render_page(self, request):
        messages = Message.objects.order_by('-message_time')[::5]
        return render(request, 'chat.html', {"messages": messages, 'form': self.form_class()})