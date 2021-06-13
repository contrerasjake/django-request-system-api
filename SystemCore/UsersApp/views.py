from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserInformation, UserInformationSerializer, UserSerializer
from rest_framework.generics import ListCreateAPIView
from django.conf import settings
from .models import User
from .serializers import UserSerializer
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.permissions import AllowAny

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

# Create your views here.
class ListUser(ListCreateAPIView):
    queryset = UserInformation.objects.all()
    serializer_class = UserInformationSerializer