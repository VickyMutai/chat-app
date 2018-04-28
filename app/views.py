from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Chat,ChatMember,ChatMessage,deserialize_user
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.
class ChatView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self,request,format=None):
        user = request.user
        chat = Chat.objects.create(admin=user)

        context = {
            'status':'SUCCESS',
            'uri':chat.uri,
            'message':'New room created'
        }
        return Response(context)

    def patch(self,request,*args,**kwargs):
        User = get_user_model()
        uri = kwargs['uri']
        username = request.data['username']
        user = User.objects.get(username=username)

        chat=Chat.objects.get(uri=uri)
        admin = chat.admin

        if admin != user:
            chat.members.get_or_create(user=user,chat=chat)

        admin = deserialize_user(admin)
        members = [ deserialize_user(chat.user) for chat in chat.members.all()]
        members.insert(0,admin)

        context = {
            'status':'SUCCESS',
            'members':members,
            'message':'%s joined that chat' %user.username,
            'user':deserialize_user(user)
        }

        return Response(context)

class ChatMessageView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        uri = kwargs['uri']
        chat = Chat.objects.get(uri=uri)
        messages = [chat_message.to_json()for chat_message in chat.messages.all()]
        context = {
            'id':chat.id,
            'uri':chat.uri,
            'messages':messages,
        }
        return Response(context)

    def post(self,request,*args,**kwargs):
        uri = kwargs['uri']
        message = request.data['message']
        user = request.user
        chat= Chat.objects.get(uri=uri)
        ChatMessage.objects.create(user=user, chat=chat, message=message)

        context={
            'status': 'SUCCESS',
            'uri': chat_session.uri, 
            'message': message,
            'user': deserialize_user(user)
        }
        return Response (context)






































