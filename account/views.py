

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

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