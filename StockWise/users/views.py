from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate

# Create your views here.

class SignUpView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = []
    def post(self, request : Request):
        data = request.data
        serializer = UserSerializer(data = data)

        if serializer.is_valid():
            serializer.save()

            response = {
                'message' : 'User has been successfully created!',
                'data' : serializer.data
            }
            return Response(data = response, status = status.HTTP_200_OK)
        
        return Response(data = serializer.data, status = status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = []

    def post(self, request):
        phonenumber = request.data.get('phonenumber')
        password = request.data.get('password')

        if not phonenumber or not password:
            return Response({"message": "Phonenumber and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=phonenumber, password=password)

        if user is not None:
            response_data = {
                'message': 'User successfully logged in!',
                'token': user.auth_token.key
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials!"}, status=status.HTTP_400_BAD_REQUEST)
