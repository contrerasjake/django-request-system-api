from django.shortcuts import render
from rest_framework import generics
from .serializers import User, UserSerializer

# Create your views here.
class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer