from django.shortcuts import render
from .models import Chat
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.db import models

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def default_view(request):
    return render(request, 'pages/default.html')

def sidebar_view(request):
    admin = User.objects.get(is_staff=True)
    users = (
        Chat.objects
        .filter(receiver=admin) 
        .values_list('sender', flat=True)
        .distinct()
    )
    senders = User.objects.filter(id__in=users)
    return render(request, "components/sidebar.html", {"users": senders})

def chat_view(request, user_id  ):
    admin = User.objects.get(is_staff=True)
    user = get_object_or_404(User, id=user_id)
    chats = Chat.objects.filter(
        models.Q(sender=admin, receiver=user) | models.Q(sender=user, receiver=admin)
    ).order_by('created_at')

    return render(request, 'pages/chat.html', {
        'user': user,
        'chats': chats
        })
