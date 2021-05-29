from django.shortcuts import render
from rest_framework import generics
from .serializers import UserInformation, UserSerializer

# Create your views here.
class ListUser(generics.ListCreateAPIView):
    queryset = UserInformation.objects.all()
    serializer_class = UserSerializer