from django.http import JsonResponse

from rest_framework.decorators import api_view

from .models import Conversation, ConversationMessage
from .serializers import ConversationListSerializer, ConversationDetailSerializer, ConversationMessageSerializer

from useraccount.models import User

@api_view(['GET'])
def conversation_list(request):
    serializer = ConversationListSerializer(request.user.conversations, many=True)

    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def conversation_detail(request, pk):
    conversation = request.user.conversations.get(pk=pk)

    conversationSerializer = ConversationDetailSerializer(conversation, many=False)
    messagesSerializer = ConversationMessageSerializer(conversation.messages.all(), many=True)

    return JsonResponse({
        'conversation': conversationSerializer.data,
        'messages': messagesSerializer.data
    }, safe=False)

@api_view(['GET'])
def conversation_start(request, user_id):
    conversations = Conversation.objects.filter(users__in=[user_id]).filter(users__in=[request.user.id])

    if conversations.count() > 0:
        conversation = conversations.first()

        return JsonResponse({'success': True, 'conversation_id': conversation.id})
    else:
        user = User.objects.get(pk=user_id)
        conversation = Conversation.objects.create()
        conversation.users.add(request.user)
        conversation.users.add(user)
        
        return JsonResponse({'success': True, 'conversation_id': conversation.id})