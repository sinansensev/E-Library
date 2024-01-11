from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(["GET", "POST"])
@permission_classes([AllowAny])
@csrf_exempt
def custom_obtain_auth_token(request):
    if request.method == "GET":
        # Handle GET requests, e.g., provide information about the login
        return Response({"message": "This is a GET request. You can provide information about login here."}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        token, created = Token.objects.get_or_create(user=user)

        refresh = RefreshToken.for_user(user)

        return Response({
            'token': token.key,
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_200_OK)

@api_view(["GET", "POST"])
def logout_user(request):
    if request.method == "GET":
        return Response({"message": "This is a GET request. You can provide information about logging out here."}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        request.user.auth_token.delete()
        return Response({"Message": "You are logged out"}, status=status.HTTP_200_OK)

@api_view(["GET", "POST"])
def user_register_view(request):
    if request.method == "GET":
        return Response({"message": "This is a GET request. You can render a form or provide information here."}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = UserRegisterSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()

            data['response'] = 'Account has been created'
            data['username'] = account.username
            data['email'] = account.email

            refresh = RefreshToken.for_user(account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            }
        else:
            data = serializer.errors

        return Response(data, status=status.HTTP_200_OK)