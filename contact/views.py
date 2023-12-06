from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import MessageSerializer
from .mailer import Mail


class CreateMessage(APIView):
    def post(self,request,*args, **kwargs):
        serializer = MessageSerializer(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            email = serializer.validated_data['email']
            title = serializer.validated_data['title']
            message = serializer.validated_data['message']
            sender = Mail(name,title,email,message)
            sender.to_client()
            sender.to_me()
            serializer.save()

            return Response({"message": "Message received successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)