from django.db import models
from users.models import CustomUser


class Message(models.Model):
    message_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message_text = models.TextField()
    message_time = models.DateTimeField()


class Chat(models.Model):
    Chat_author = models.ForeignKey(CustomUser, related_name='chat_author_set', on_delete=models.CASCADE)
    Chat_users = models.ManyToManyField(CustomUser)
    Chat_name = models.CharField(max_length=30)


