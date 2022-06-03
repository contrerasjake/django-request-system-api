from typing import ContextManager
from django.shortcuts import render
from django.contrib import auth
from django.conf import settings
from rest_framework import viewsets, generics, permissions, status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserInformationSerializer, UserSerializer, LogoutSerializer, LoginSerializer, ChangePasswordSerializer, AccountStatusSerializer
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generate_token
from django.core.mail import EmailMessage
from django.conf import settings
import threading

class EmailThread(threading.Thread):
    def __init__(self,email):
        self.email = email
        threading.Thread.__init__(self)
    
    def run(self):
        self.email.send()

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('usersapp/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email=EmailMessage(subject=email_subject,body=email_body,from_email=settings.EMAIL_FROM_USER,to=[user.email])
    EmailThread(email).start()

def activate_user(request, uidb64, token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)

    except Exception as e:
        user=None

    if not user.is_email_verified and generate_token.check_token(user,token):
        user.is_email_verified = True
        user.save()

        return render(request, 'usersapp/activation-success.html')
    
    if user.is_email_verified and generate_token.check_token(user,token):

        return render(request, 'usersapp/account-activated.html')
    
    return render(request, 'usersapp/activate-failed.html')

class ResendEmailVerification(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserInformationSerializer
    queryset = User.objects.all()

    def get(self, request):
        serializer = self.serializer_class(request.user)
        user = User.objects.get(email=serializer.data.get('email'))
        send_activation_email(user, request)
        return Response(status=status.HTTP_200_OK)

class CheckAccountStatus(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccountStatusSerializer
    queryset = User.objects.all()

    def get(self, request):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegisterView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(email=serializer.data.get('email'))
            send_activation_email(user, request)
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

class UserListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserInformationSerializer
    queryset = User.objects.all()

class ChangePasswordView(generics.UpdateAPIView):

    queryset = User.objects.all()
    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = queryset.get(pk=self.request.user.id)
        self.check_object_permissions(self.request, obj)
        return obj
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer