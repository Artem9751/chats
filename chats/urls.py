from django.urls import path
from .views import HomeChatView, CreateChatView

urlpatterns = [
    path('', HomeChatView.as_view(), name='chat'),
    path('createchat/', CreateChatView.as_view(), name='createchat')
]