from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate-user/<uidb64>/<token>', activate_user, name='activate'),
    path('resend-activation/', ResendEmailVerification.as_view()),
    path('account-status/', CheckAccountStatus.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('getuser/', UserInformationView.as_view()),
    path('change_password/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('list/', UserListView.as_view()),
    path('list/<int:pk>/', UserListView.as_view()),
    path('sendemail/', MailSenderView.as_view()),
]