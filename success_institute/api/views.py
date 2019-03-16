from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
<<<<<<< HEAD
import json
from django.core import serializers
=======
from django.contrib.auth.models import User
>>>>>>> master


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)

    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)

    context = {'token': token.key, 'user': {
        'username': user.username,
        'email': user.email
    }}
    return Response(context,
                    status=HTTP_200_OK)
<<<<<<< HEAD


@csrf_exempt
@api_view(["POST"])
def hello(request):
    return Response({'token': "hello_word"}, status=HTTP_200_OK)
=======
@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    user = User.username
    data = {'user': user}
    return Response(data, status=HTTP_200_OK)
>>>>>>> master
