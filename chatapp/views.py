from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ChatRoom

# Create your views here.


def home(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'chatapp/index.html', {'chatrooms': chatrooms})



def chatRoom(request, slug):
    chatroom = ChatRoom.objects.get(slug=slug)
    return render(request, 'chatapp/chatroom.html', {'chatroom': chatroom})