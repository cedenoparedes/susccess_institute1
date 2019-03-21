from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from api.serializers import StudentSerializer, GroupSerializer
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from api.models import Student, Group
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)


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
        'Nomber': user.first_name,
        'email': user.email
    }}

    return Response(context,
                    status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
def add_student(request):
    data = JSONParser().parse(request)
    serializer = StudentSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors,status=400)

@csrf_exempt
@api_view(["GET"])
def get_student_list(request):

    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
@api_view(["GET"])
def group_list(request):

    group = Group.objects.all()
    serializer = GroupSerializer(group, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@api_view(["POST"])
def save_group(request):
    data = JSONParser().parse(request)
    serializer = GroupSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)



