from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Message, Chat, CustomUser
from .forms import MessageForm, ChatCreateForm
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


class CreateChatView(CreateView):
    model = Chat
    form_class = ChatCreateForm
    template_name = 'createchat.html'

    def post(self, request):
        """ Check for valid data, create new chat and redirect"""
        add_user_list = CustomUser.objects.order_by('username')
        chatform = ChatCreateForm(request.POST)
        #if chatform.is_valid():
            #chat = Chat()
            #chatuser = CustomUser.objects.get(username=request.POST.get("user"))
            #owner = request.user.username
            #chat = Chat.objects.create(name=request.POST.get("name"), owner=owner)
            #chat.user.add(user)
        return render(request, self.template_name, {"chatform": chatform, 'adduserlist': add_user_list})


    def get(self, request):
        users = CustomUser.objects.filter(username__startswith='t')
        print(users)
        Chat.objects.create(Chat_author=users.first(), Chat_name='asdas')
        a = Chat.objects.filter(Chat_author__id=2)
        print(a.query)
        add_user_list = CustomUser.objects.order_by('username')
        # for i in range(20):
        #     CustomUser.objects.create(username=f'test+{i}')
        chatform = ChatCreateForm()
        return render(request, 'createchat.html', {"chatform": chatform, 'adduserlist': add_user_list})