

# Create your views here.
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Note
from .serializers import NoteSerializer




@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def signup(request):

    form = UserCreationForm(data=request.data)

    if form.is_valid():
        user = form.save()
        token = Token.objects.create(user=user)

        return Response({
            "message": "Account created successfully",
            "token": token.key
        }, status=status.HTTP_201_CREATED)

    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def login(request):

    username = request.data.get("username")
    password = request.data.get("password")

    if username is None or password is None:
        return Response(
            {"error": "Please provide username and password"},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = authenticate(username=username, password=password)

    if not user:
        return Response(
            {"error": "Invalid Credentials"},
            status=status.HTTP_404_NOT_FOUND
        )

    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        "message": "Login successful",
        "token": token.key,
        "username": user.username
    }, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated,))
def add_note(request):

    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(
            {"message": "Note added successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated,))
def list_notes(request):

    notes = Note.objects.filter(user=request.user)
    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data)
