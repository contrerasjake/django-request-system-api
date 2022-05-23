from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import LogoutAPIView, LoginView, RegisterView, UserInformationView, ChangePasswordView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
    path('getuser/', UserInformationView.as_view()),
    path('change_password/', ChangePasswordView.as_view(), name='auth_change_password'),
]