from django.urls import path
from .views import ListUser, ListUserView, RegisterView, LoginView

urlpatterns = [
    path('', ListUser.as_view(), name='Users'),
    path('<int:pk>/', ListUserView.as_view(), name='SingleUser'),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view())
]