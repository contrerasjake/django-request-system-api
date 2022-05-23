from typing import ContextManager
from django.shortcuts import render
from django.contrib import auth
from django.conf import settings
from rest_framework import viewsets, generics, permissions, status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserInformationSerializer, UserSerializer, LogoutSerializer, LoginSerializer, ChangePasswordSerializer
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser

# class RegisterView(generics.GenericAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]

#     def post(self, request):

#         serializer = UserSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

class UserInformationView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserInformationSerializer
    queryset = User.objects.all()
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer