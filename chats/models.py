from django.db import models
from users.models import CustomUser


class Message(models.Model):
    message_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message_text = models.TextField()
    message_time = models.DateTimeField()

