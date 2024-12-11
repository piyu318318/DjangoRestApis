from django.shortcuts import render, HttpResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken  # import JWT using which generates the access token as well as refresh token
from django.contrib.auth.hashers import check_password
from .models import Users
from rest_framework.permissions import IsAuthenticated  # requires the
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterUser(APIView):  # inherit the views

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!", "status": "200"},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomePage(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home Page")


class LoginUser(APIView):
    def post(self, request):
        userName = request.data.get('userName')
        password = request.data.get('password')
        try:
            user = Users.objects.get(userName=userName)

            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)
                return Response({
                    "message": "user login successfully",
                    "access": str(refresh.access_token),
                    "refresh": str(refresh),
                    "status": "200"
                })
            else:
                return Response({"message": "Invalid password.", "status": "401"}, status=status.HTTP_401_UNAUTHORIZED)

        except Users.DoesNotExist:
            return Response({"message": "User not found.", "status": "404"}, status=status.HTTP_404_NOT_FOUND)


