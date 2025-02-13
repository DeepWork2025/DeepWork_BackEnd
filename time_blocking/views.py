from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.contrib.auth import authenticate
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['POST'])
def register_view(request):
    '''
    user regisert with API, if register successfully, return tokens
    '''
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'Successfully registered!',
            'access': str(refresh.access_token),  # return access_token
            'refresh': str(refresh),  # return refresh_token
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    '''
    User login with API, if login succesfully, return tokens
    '''
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'Login successful',
            'access': str(refresh.access_token),  # return access_token
            'refresh': str(refresh),  # return refresh_token
        }, status=status.HTTP_200_OK)
    
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
