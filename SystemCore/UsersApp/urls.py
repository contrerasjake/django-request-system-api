from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, LogoutAPIView, LoginView
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token_verify'),
]