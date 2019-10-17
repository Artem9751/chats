from django.urls import path
from .views import HomeChatView

urlpatterns = [
    path('', HomeChatView.as_view(), name='chat'),
    #path('/chats', TemplateView.as_view(), name='HomePage'),
]