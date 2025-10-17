from django.db import models
from django.contrib.auth.models import User

# class ChatRoom(models.Model):
#     ROOM_CHOICES = [
#         ('private', 'Private'),
#         ('group', 'Group'),
#     ]

#     name = models.CharField(max_length=255)
#     room_type = models.CharField(max_length=1, choices=ROOM_CHOICES)
#     members = models.ManyToManyField(User, related_name='chat_rooms')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return {self.id}

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_chats')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_chats')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.sender.username} to {self.receiver.username}"